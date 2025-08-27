import type { InsightRequestProps } from "../types";

const API_ENDPOINT = import.meta.env.VITE_API_ENDPOINT;
const API_KEY = import.meta.env.VITE_API_KEY;

export const generateInsight = async (data: InsightRequestProps): Promise<string> => {
    const response = await fetch(API_ENDPOINT, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-Api-Key": API_KEY
        },
        body: JSON.stringify(data)
    });

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || `HTTP Error ${response.status}`);
    }

    return JSON.parse(await response.text())["insight"];
};