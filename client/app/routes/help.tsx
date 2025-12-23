import { usePageContentAndSiteInfo } from "../api/pageContent";

const HelpPage = () => {
  const { pageContent } = usePageContentAndSiteInfo();
  return (
    <div
      className="col well content-well"
      dangerouslySetInnerHTML={{ __html: pageContent.pageContent || "" }}
    />
  );
};

export default HelpPage;
