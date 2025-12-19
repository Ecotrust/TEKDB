export type PageContentResponse = {
  page: string;
  pageTitle: string;
  pageContent: string; // May contain HTML
};

const baseUrl = (import.meta.env.VITE_API_BASE_URL as string) || "";

export async function fetchPageContent(
  name: string,
  signal?: AbortSignal
): Promise<PageContentResponse> {
  const url = `${baseUrl}/api/page/${encodeURIComponent(name)}/`;
  const res = await fetch(url, { signal, credentials: "include" });
  if (!res.ok) {
    throw new Error(`Failed to fetch page content: ${res.status}`);
  }
  return res.json();
}

export async function fetchSiteInfo(signal?: AbortSignal): Promise<any> {
  const url = `${baseUrl}/api/site-info/`;
  const res = await fetch(url, { signal, credentials: "include" });
  if (!res.ok) {
    throw new Error(`Failed to fetch site info: ${res.status}`);
  }
  return await res.json();
}
