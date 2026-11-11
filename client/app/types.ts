const Category = {
    Place: "Place",
    Resource: "Resource",
    Citations: "Citations",
    Activity: "Activity",
    Media: "Media"
} as const;

export type Category = typeof Category[keyof typeof Category];

const ResultType = {
    ResourcesActivityEvents: "Resourcesactivityevents",
    Resources: "resources",
    Media: "media",
    Citations: "citations",
    Places: "places"
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