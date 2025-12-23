import axios, {
  AxiosError,
  type AxiosResponse,
  type InternalAxiosRequestConfig,
} from "axios";
import { redirect } from "react-router";

const baseURL =
  (import.meta.env.VITE_API_BASE_URL as string) || `http://localhost:8000/`;

export const tekdbApi = axios.create({
  baseURL,
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFToken",
  withCredentials: true,
});

// interceptor to apply auth token to axios requests
tekdbApi.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    config.headers = config.headers ?? {};
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export const returnOnSuccess = (response: AxiosResponse) => response;

export const redirectOnUnauthorized = (error: AxiosError) => {
  if (error.response?.status === 401) {
    redirect("/login_async/");
  }
  return Promise.reject(error);
};

tekdbApi.interceptors.response.use(returnOnSuccess, redirectOnUnauthorized);

// Helper to prime CSRF cookie and token
export async function primeCsrf(): Promise<string> {
  const resp = await tekdbApi.get("/api/csrf/");
  const token = (resp.data?.csrfToken as string) || "";

  return token;
}
