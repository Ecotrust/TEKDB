import React, {
  createContext,
  useCallback,
  use,
  useState,
} from "react";
import type { ReactNode } from "react";
import {useLocation} from "react-router";
import type { FilterCategories, Result } from "../types";
import { useNavigate } from "react-router";
import { submitSearchAction } from "./action";
import { CATEGORIES } from "../types";

type useSearch = {
  categories: FilterCategories[];
  results: Result[];
  query: string;
  searchedQuery: string;
  handleCategoryTypeChange: (type: FilterCategories) => void;
  handleSearch: () => Promise<void>;
  handleQueryChange: (query: string) => void;
  handleCategoryAndSearch: (type: FilterCategories) => void;
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
        return categories.filter((category: FilterCategories) => category !== type);
      } else {
        setCategories([...categories, type]);
        return [...categories, type];
      }
    },
    [categories],
  );

  const handleQueryChange = useCallback((query: string) => {
    setQuery(query);
  }, []);

  const handleSearch = useCallback(async (categoriesToSearch?: FilterCategories[]) => {
    try {
      const response = await submitSearchAction({ categories: categoriesToSearch ?? categories, query });
      const { results } = response;
      setResults(results);
      setSearchedQuery(query); // update the executed searched query
      if (location.pathname !== "/search") {
        await navigate("/search");
      }
    } catch (error) {
      console.error("Search failed", error);
    }
  }, [categories, query, location]);

  const handleCategoryAndSearch = useCallback(
    (category: FilterCategories) => {
      const newCategories = categories.includes(category)
        ? categories.filter((c: FilterCategories) => c !== category)
        : [...categories, category];
      handleSearch(newCategories);
      handleCategoryTypeChange(category);
    },
    [categories, handleSearch, handleCategoryTypeChange]
  );
  
  const value = {
    categories,
    results,
    query,
    searchedQuery,
    handleCategoryAndSearch,
    handleSearch,
    handleQueryChange,
    handleCategoryTypeChange,
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
