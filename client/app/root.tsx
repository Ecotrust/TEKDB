import {
  isRouteErrorResponse,
  Links,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
  useLoaderData,
} from "react-router";

import type { Route } from "./+types/root";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import {
  fetchPageContentAndSiteInfo,
  type PageContentAndSiteInfo,
} from "./api/pageContent";

export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <Meta />
        <Links />
      </head>
      <body>
        {children}
        <ScrollRestoration />
        <Scripts />
      </body>
    </html>
  );
}

export const RouteToPath: Record<string, string> = {
  about: "/About",
  help: "/Help",
  welcome: "/Welcome",
};

export async function loader({ request }: Route.LoaderArgs) {
  const url = new URL(request.url);
  const [, path] = url.pathname.split("/");
  const pageContent = await fetchPageContentAndSiteInfo(
    RouteToPath[path as keyof typeof RouteToPath] || "/Welcome"
  );
  return pageContent;
}

export default function Root() {
  const { pageContent, siteInfo } = useLoaderData<typeof loader>();

  return (
    <>
      <style
        dangerouslySetInnerHTML={{
          __html: `
        :root {
          ${
            siteInfo?.proj_css
              ? Object.entries(siteInfo.proj_css)
                  .map(([key, value]) => `--${key}: ${value};`)
                  .join("\n")
              : ""
          }
          ${
            siteInfo
              ? `--home_font_color: ${siteInfo.home_font_color};
               --homepage_right_background: ${siteInfo.homepage_right_background};
               --homepage_left_background: ${siteInfo.homepage_left_background};`
              : ""
          }
        `,
        }}
      />
      <Outlet
        context={{ pageContent, siteInfo } satisfies PageContentAndSiteInfo}
      />
    </>
  );
}

export function ErrorBoundary({ error }: Route.ErrorBoundaryProps) {
  let message = "Oops!";
  let details = "An unexpected error occurred.";
  let stack: string | undefined;

  if (isRouteErrorResponse(error)) {
    message = error.status === 404 ? "404" : "Error";
    details =
      error.status === 404
        ? "The requested page could not be found."
        : error.statusText || details;
  } else if (import.meta.env.DEV && error && error instanceof Error) {
    details = error.message;
    stack = error.stack;
  }

  return (
    <>
      <main className="content-wrapper">
        <div className="container content-container">
          <div className="row content-row">
            <div className="col well content-well">
              <h1>{message}</h1>
              <p>{details}</p>
              {stack && <pre style={{ whiteSpace: "pre-wrap" }}>{stack}</pre>}
            </div>
          </div>
        </div>
      </main>
    </>
  );
}
