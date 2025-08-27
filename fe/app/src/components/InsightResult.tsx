import type { FC } from 'react';
import Markdown from 'react-markdown';
import type { InsightDisplayProps } from '../types';

const InsightResultDisplay: FC<InsightDisplayProps> = ({ insightText }) => (
    <div className="mt-8 w-full animate-fade-in">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">Generated Insight</h2>
        <div className="bg-white p-6 rounded-lg shadow-md border border-gray-200">
            <div>
                <Markdown>
                    {insightText}
                </Markdown>
            </div>
        </div>
    </div>
);

export default InsightResultDisplay;