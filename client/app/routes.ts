import { type RouteConfig, route, layout } from "@react-router/dev/routes";

export default [
  layout("layouts/explore.tsx", [
    route("", "./routes/welcome.tsx"),
    route("about", "./routes/about.tsx"),
    route("help", "./routes/help.tsx"),
    route("", "layouts/private-route.tsx", [
      route("explore", "./routes/explore.tsx"),
      route("search", "./routes/search.tsx"),
    ]),
  ]),
] satisfies RouteConfig;
