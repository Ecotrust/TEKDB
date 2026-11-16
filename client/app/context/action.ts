import axios from "axios";
import { primeCsrf, tekdbApi } from "../api/tekdbApi";
import type { FilterCategories } from "../types";

export type LoginState = {
  success?: boolean;
  error?: string | null;
};

export const submitLoginAction = async (
  prevState: LoginState,
  formData: FormData
): Promise<LoginState> => {
  const username = String(formData.get("username") ?? "");
  const password = String(formData.get("password") ?? "");

  // Prime CSRF cookie/token first
  const csrfToken = await primeCsrf();

  // Use form-encoded body
  const body = new URLSearchParams();
  body.append("username", username);
  body.append("password", password);

  try {
    const login = await tekdbApi.post("/login_async/", body, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRFToken": csrfToken,
      },
      withCredentials: true,
    });

    if (login.status === 200 && login.data.success) {
      return { ...prevState, success: true, error: null };
    }

    return {
      ...prevState,
      success: false,
      error: login.data.error || "Invalid username or password",
    };
  } catch (error) {
    if (axios.isAxiosError(error) && error.response?.status === 401) {
      return {
        ...prevState,
        success: false,
        error: "Invalid username or password",
      };
    }

    return {
      ...prevState,
      success: false,
      error: "Unable to log in right now. Please try again.",
    };
  }
};

export const submitSearchAction = async ({ categories, query }: { categories: FilterCategories[], query: string }) => {
  const params = new URLSearchParams({ query });
  categories.forEach((category) => params.append("category", category));

  try {
    const response = await tekdbApi.get("/api/search/", {
      params,
    });

    if (response.status === 200) {
      return response.data;
    }

    throw new Error("Search failed");
  } catch (error) {
    console.error("Search error", error);
    throw error;
  }
};