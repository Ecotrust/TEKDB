import type React from "react";
import { Outlet } from "react-router";
import Header from "../components/header";
import { usePageContentAndSiteInfo } from "../api/pageContent";

const ExploreLayout: React.FC = () => {
  const { pageContent, siteInfo } = usePageContentAndSiteInfo();
  const isAuthenticated = false; // TODO: Replace with actual authentication logic

  return (
    <>
      <Header
        projIcons={siteInfo?.proj_icons || { logo: "" }}
        projTextPlacement={siteInfo?.proj_text_placement || "top"}
        projLogoText={siteInfo?.proj_logo_text || ""}
        isAuthenticated={isAuthenticated}
        pageTitle={pageContent?.pageTitle || "Explore"}
      />
      <main className="content-wrapper">
        <div className="container content-container">
          <div className="row content-row">
            <Outlet context={{ pageContent, siteInfo }} />
          </div>
        </div>
      </main>
    </>
  );
};

export default ExploreLayout;
