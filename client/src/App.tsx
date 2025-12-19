import { useEffect, useState } from "react";
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
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [data, setData] = useState<PageContentResponse | null>(null);
  const [siteInfo, setSiteInfo] = useState<any | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const setCSSVariables = (theme: Record<string, string>) => {
    if (!theme) return;
    Object.entries(theme).forEach(([key, value]) => {
      document.documentElement.style.setProperty(`--${key}`, value);
    });
  };

  useEffect(() => {
    const controller = new AbortController();

    setLoading(true);
    setError(null);
    setData(null);
    fetchPageContent(pageName, controller.signal)
      .then((resp) => setData(resp))
      .catch((e) => {
        if (e.name !== "AbortError") {
          console.error("Error fetching page content:", e);
          setError("Failed to load page content.");
        }
      })
      .finally(() => setLoading(false));

    return () => controller.abort();
  }, [pageName]);

  useEffect(() => {
    const controller = new AbortController();

    fetchSiteInfo(controller.signal)
      .then((resp) => {
        setSiteInfo(resp);
        if (resp.proj_css) {
          setCSSVariables(resp.proj_css);
          setCSSVariables({["home_font_color"]: resp.home_font_color, ["homepage_right_background"]: resp.homepage_right_background, ["homepage_left_background"]: resp.homepage_left_background})
        }
      })
      .catch((e) => {
        if (e.name !== "AbortError") {
          console.error("Error fetching site info:", e);
          setError("Failed to load site information.");
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
        isAuthenticated={isAuthenticated}
      />
      <main className="content-wrapper">
        <div className="container content-container">
          <div className="row content-row">
            <div className="col well content-well">
              {loading && <p>Loading…</p>}
              {error && <p style={{ color: "red" }}>Error: {error}</p>}
              {!loading && !error && data && (
                <div className="container">
                  <div className="row gx-4 align-items-center">
                    <div
                      className="col-lg-5 homepage-column"
                      id="homepage-left-column"
                    >
                      <div
                        className="welcome-content-wrapper"
                        dangerouslySetInnerHTML={{ __html: data.pageContent }}
                      ></div>
                      <div className="welcome-login-button-wrapper">
                        {!isAuthenticated ? (
                          <button
                            type="button"
                            className="btn welcome-login-btn"
                            data-bs-toggle="modal"
                            data-bs-target="#loginModal"
                          >
                            Login <span className="arrow-right"></span>
                          </button>
                        ) : (
                          <a
                            href="/explore"
                            type="button"
                            className="btn welcome-login-btn"
                          >
                            Explore <span className="arrow-right"></span>
                          </a>
                        )}
                      </div>
                    </div>
                    <div
                      className="col-lg-7 homepage-column"
                      id="homepage-right-column"
                    >
                      <div className="proj-image-select-wrapper">
                        <img
                          src={`http://127.0.0.1:8000${siteInfo?.proj_image_select || ""}`}
                          alt="project image"
                        ></img>
                      </div>
                      {siteInfo && siteInfo.home_image_attribution && (
                        <div id="proj-image-attribution">
                          <a
                            className="attribution-toggle"
                            data-bs-toggle="collapse"
                            href="#collapseAttribution"
                            role="button"
                            aria-expanded="false"
                            aria-controls="collapseAttribution"
                          >
                            <i className="bi bi-info-circle"></i>
                          </a>
                          <div className="collapse" id="collapseAttribution">
                            <p>{siteInfo.home_image_attribution}</p>
                          </div>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </main>
    </>
  );
}

export default App;
