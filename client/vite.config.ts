import { defineConfig } from "vite";
import { reactRouter } from "@react-router/dev/vite";

const apiProxyTarget =
  process.env.VITE_API_PROXY_TARGET ||
  process.env.VITE_API_BASE_URL ||
  "http://localhost:8000";

// https://vite.dev/config/
export default defineConfig({
  plugins: [reactRouter()],
  server: {
    proxy: {
      // forward API calls to Django dev server
      "/api": {
        target: apiProxyTarget,
        changeOrigin: true,
        secure: false,
      },
    },
  },
});
