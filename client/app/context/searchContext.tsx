import React, {
  createContext,
  useCallback,
  use,
  useState,
  useMemo,
} from "react";
import type { ReactNode } from "react";
import {useLocation} from "react-router";
import type { FilterCategories, Result } from "../types";
import { CategoryToFilterCategoryMap } from "../types";
import { useNavigate } from "react-router";
import { submitSearchAction } from "./action";
import { CATEGORIES } from "../types";

type useSearch = {
  categories: FilterCategories[];
  results: Result[];
  filteredResults: Result[];
  query: string;
  searchedQuery: string;
  handleCategoryTypeChange: (type: FilterCategories) => void;
  handleSearch: () => Promise<void>;
  handleQueryChange: (query: string) => void;
};

const SearchContext = createContext<useSearch | null>(null);

interface SearchProviderProps {
  children: ReactNode;
}

export const SearchProvider: React.FC<SearchProviderProps> = ({ children }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const [categories, setCategories] = useState<FilterCategories[]>(CATEGORIES);
  const [results, setResults] = useState<Result[]>([]);
  const [query, setQuery] = useState<string>(""); // search query input by the user
  const [searchedQuery, setSearchedQuery] = useState<string>(""); // the executed searched query

  const handleCategoryTypeChange = useCallback(
    (type: FilterCategories) => {
      if (categories.includes(type)) {
        setCategories(
          categories.filter((category: FilterCategories) => category !== type),
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
      setSearchedQuery(query); // update the executed searched query
      if (location.pathname !== "/search") {
        await navigate("/search");
      }
    } catch (error) {
      console.error("Search failed", error);
    }
  }, [categories, query, navigate]);

  const filteredResults = useMemo(() => {
    return results.filter((result) =>
      categories.includes(CategoryToFilterCategoryMap[result.category_name]),
    );
  }, [results, categories]);
  
  const value = {
    categories,
    results,
    filteredResults,
    query,
    searchedQuery,
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
