import { usePageContentAndSiteInfo } from "../api/pageContent";

const AboutPage = () => {
  const { pageContent } = usePageContentAndSiteInfo();
  return (
    <div
      className="col well content-well"
      dangerouslySetInnerHTML={{ __html: pageContent.pageContent || "" }}
    />
  );
};

export default AboutPage;
