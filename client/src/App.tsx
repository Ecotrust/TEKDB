import { use, useEffect, useMemo, useState } from "react";
import "./App.css";
import {
  fetchPageContent,
  fetchSiteInfo,
  type PageContentResponse,
} from "./api/pageContent";
import Header from "./components/header";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  const [pageName, setPageName] = useState<"Welcome" | "About" | "Help">(
    "Welcome",
  );
  const [data, setData] = useState<PageContentResponse | null>(null);
  const [siteInfo, setSiteInfo] = useState<any | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const setCSSVariables = (theme: Record<string, string>) => {
    for (const value in theme) {
      document.documentElement.style.setProperty(`--${value}`, theme[value]);
    }
  };

  useEffect(() => {
    const controller = new AbortController();

    setLoading(true);
    setError(null);
    setData(null);
    fetchPageContent(pageName, controller.signal)
      .then((resp) => setData(resp))
      .catch((e) => {
        if (e.name !== "AbortError") setError(String(e));
      })
      .finally(() => setLoading(false));
    return () => controller.abort();
  }, [pageName]);

  useEffect(() => {
    const controller = new AbortController();
    console.log("Fetching Site Info");
    fetchSiteInfo(controller.signal)
      .then((resp) => {
        setSiteInfo(resp);
        if (resp.proj_css) {
          setCSSVariables(resp.proj_css);
        }
      })
      .catch((e) => {
        if (e.name !== "AbortError") {
          console.error("Site info error:", e);
          setError(String(e));
        }
      });
    return () => controller.abort();
  }, []);

  return (
    <>
      <Header
        projIcons={siteInfo?.proj_icons || { logo: "" }}
        projTextPlacement={siteInfo?.proj_text_placement || "top"}
        projLogoText={siteInfo?.proj_logo_text || ""}
        pageTitle={pageName}
        setPageName={setPageName}
        isAuthenticated={false}
      />
      <main>
        {loading && <p>Loading…</p>}
        {error && <p style={{ color: "red" }}>Error: {error}</p>}
        {!loading && !error && data && (
          <article>
            {/* pageContent may include HTML from admin; rendering as HTML intentionally */}
            <div dangerouslySetInnerHTML={{ __html: data.pageContent }} />
          </article>
        )}
      </main>
    </>
  );
}

export default App;
