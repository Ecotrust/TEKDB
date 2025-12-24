import { primeCsrf, tekdbApi } from "../api/tekdbApi";

export type LoginState = {
  success?: boolean;
  error?: string | null;
};

export const submitAction = async (
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

  const login = await tekdbApi.post("/login_async/", body, {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "X-CSRFToken": csrfToken,
    },
    withCredentials: true,
  });

  if (
    login.status !== 200 ||
    login.statusText !== "OK" ||
    !login.data.success
  ) {
    return {
      ...prevState,
      success: false,
      error: login.data.error || "Invalid username or password",
    };
  } else if (login.status == 200) {
    return { ...prevState, success: true, error: null };
  }
  return {
    ...prevState,
    success: false,
    error: "Invalid username or password",
  };
};
