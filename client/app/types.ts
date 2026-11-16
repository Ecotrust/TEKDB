const Category = {
    Place: "Place",
    Resource: "Resource",
    Source: "Source",
    Activity: "Activity",
    Media: "Media"
} as const;

const FilterCategories = {
    places: "places",
    resources: "resources",
    sources: "sources",
    activities: "activities",
    media: "media"
} as const;

export const CATEGORIES = Object.values(FilterCategories);

export type FilterCategories = typeof FilterCategories[keyof typeof FilterCategories];

export type Category = typeof Category[keyof typeof Category];

const ResultType = {
    Places: "places",
    Resources: "resources",
    Citations: "citations",
    ResourcesActivityEvents: "Resourcesactivityevents",
    Media: "media",
} as const;

export const CategoryToFilterCategoryMap = {
    Place: FilterCategories.places,
    Resource: FilterCategories.resources,
    Source: FilterCategories.sources,
    Activity: FilterCategories.activities,
    Media: FilterCategories.media
} as const; 

export type ResultType = typeof ResultType[keyof typeof ResultType];

export type Result = {
    category_name: Category;
    description: string;
    headline: string;
    id: number;
    image: string;
    link: string;
    name: string;
    rank: number;
    similarity: number;
    type: ResultType;
}