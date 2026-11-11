import React, { useCallback, use } from "react";
import type { ReactNode } from "react";
import { useNavigate } from "react-router";
import { submitSearchAction } from "./action";

type useSearch = {
  categories: string[];
  results: any[];
  query: string;
  handleCategoryTypeChange: (type: string) => void;
  handleSearch: (formData: FormData) => Promise<void>;
  handleQueryChange: (query: string) => void;
};

const SearchContext = React.createContext<useSearch | null>(null);

interface SearchProviderProps {
  children: ReactNode;
}

export const SearchProvider: React.FC<SearchProviderProps> = ({ children }) => {
  const navigate = useNavigate();
  const [categories, setCategories] = React.useState<string[]>([]);
  const [results, setResults] = React.useState<any[]>([]);
  const [query, setQuery] = React.useState<string>("");

  const handleCategoryTypeChange = useCallback(
    (type: string) => {
      if (categories.includes(type)) {
        setCategories(
          categories.filter((category: string) => category !== type),
        );
      } else {
        setCategories([...categories, type]);
      }
    },
    [categories],
  );

  const handleQueryChange = useCallback((query: string) => {
    setQuery(query);
  }, []);

  const handleSearch = useCallback(async () => {
    try {
      const response = await submitSearchAction({ categories, query });
      const { results } = response;
      setResults(results);
      await navigate("/search");
    } catch (error) {
      console.error("Search failed", error);
    }
  }, [categories, query, navigate]);

  const value = {
    categories,
    results,
    query,
    handleCategoryTypeChange,
    handleSearch,
    handleQueryChange,
  };
  return <SearchContext value={value}>{children}</SearchContext>;
};

export const useSearch = () => {
  const context = use(SearchContext);
  if (!context) {
    throw new Error("useSearch must be used within a SearchProvider");
  }
  return context;
};
