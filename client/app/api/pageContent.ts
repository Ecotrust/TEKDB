import { useOutletContext } from "react-router";

export type PageContentResponse = {
  page: string;
  pageTitle: string;
  pageContent: string;
};

export type SiteInfoResponse = {
  proj_logo_text: string;
  proj_text_placement: string;
  proj_css: Record<string, string>;
  proj_icons: {
    logo: string;
    place_icon: string;
    resource_icon: string;
    activity_icon: string;
    source_icon: string;
    media_icon: string;
  };
  proj_image_select: string;
  home_image_attribution: string;
  home_font_color: string;
  homepage_right_background: string;
  homepage_left_background: string;
  map_pin: string;
  map_pin_selected: string;
};

export type PageContentAndSiteInfo = {
  pageContent: PageContentResponse;
  siteInfo: SiteInfoResponse;
};

// TODO: fix baseUrl to use env variable
const baseUrl = "http://localhost:8000";

export async function fetchPageContent(
  path: string
): Promise<PageContentResponse> {
  const url = `${baseUrl}/api/page${path}/`;
  const res = await fetch(url, { credentials: "include" });
  if (!res.ok) {
    throw new Error(`Failed to fetch page content: ${res.status}`);
  }
  return res.json();
}

export async function fetchSiteInfo(): Promise<SiteInfoResponse> {
  const url = `${baseUrl}/api/site-info/`;
  const res = await fetch(url, { credentials: "include" });
  if (!res.ok) {
    throw new Error(`Failed to fetch site info: ${res.status}`);
  }
  return await res.json();
}

export async function fetchPageContentAndSiteInfo(path: string): Promise<{
  pageContent: PageContentResponse;
  siteInfo: SiteInfoResponse;
}> {
  const [pageContent, siteInfo] = await Promise.all([
    fetchPageContent(path),
    fetchSiteInfo(),
  ]);
  return { pageContent, siteInfo };
}

export const usePageContentAndSiteInfo = () => {
  return useOutletContext<PageContentAndSiteInfo>();
};
