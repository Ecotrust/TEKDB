import { type RouteConfig, route, layout } from "@react-router/dev/routes";

export default [
  layout("layouts/explore.tsx", [
    route("", "./routes/welcome.tsx"),
    route("about", "./routes/about.tsx"),
    route("help", "./routes/help.tsx"),
  ]),
] satisfies RouteConfig;
