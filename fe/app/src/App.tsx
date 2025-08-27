import React, { useState } from 'react';
import type { FC } from 'react';
import Spinner from './components/Spinner';
import ErrorMessage from './components/Error';
import InsightResultDisplay from './components/InsightResult';
import { generateInsight } from './services/apiServices';

const App: FC = () => {
	const [companyUrl, setCompanyUrl] = useState<string>('');
	const [userNotes, setUserNotes] = useState<string>('');
	const [insight, setInsight] = useState<string | null>(null);
	const [isLoading, setIsLoading] = useState<boolean>(false);
	const [error, setError] = useState<string | null>(null);

	const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
		e.preventDefault();
		setIsLoading(true);
		setError(null);
		setInsight(null);

		try {
			const textData = await generateInsight({
				company_url: companyUrl,
				user_notes: userNotes,
			});
		
			setInsight(textData);
		} catch (err) {
			if (err instanceof Error) {
				setError(err.message);
			}
		} finally {
			setIsLoading(false);
		}
	};

	return (
		<div className="bg-gray-50 min-h-screen flex flex items-center justify-center font-sans">
			<div className="w-full max-w-3xl mx-2">
				<div className="bg-white p-8 rounded-xl shadow-lg border border-gray-200">
		
					<div className="text-center mb-8">
						<h1 className="text-3xl font-bold text-gray-800">Company Profiler</h1>
						<p className="text-gray-500 mt-2">Enter a company URL and your notes to generate an AI-powered analysis.</p>
					</div>

					<form onSubmit={handleSubmit}>
						<div className="space-y-6">
							<div>
								<label htmlFor="companyUrl" className="block text-sm font-medium text-gray-700 mb-1">
									Company Website URL
								</label>
								<input
									type="url"
									id="companyUrl"
									value={companyUrl}
									onChange={(e: React.ChangeEvent<HTMLInputElement>) => setCompanyUrl(e.target.value)}
									className="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:shadow-xl transition"
									placeholder="https://www.example.com"
									required
								/>
							</div>
						
							<div>
								<label htmlFor="userNotes" className="block text-sm font-medium text-gray-700 mb-1">
									Your Ideal Customer Profile or Notes (Optional)
								</label>
								<textarea
									id="userNotes"
									value={userNotes}
									onChange={(e: React.ChangeEvent<HTMLTextAreaElement>) => setUserNotes(e.target.value)}
									className="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:shadow-xl transition"
									placeholder="e.g., B2B SaaS company with over 50 employees..."
								></textarea>
							</div>
						</div>

						<div className="mt-8">
							<button
								type="submit"
								disabled={isLoading}
								className="w-full flex items-center justify-center px-6 py-3 border font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 hover:cursor-pointer transition"
							> 
								{isLoading ? <Spinner /> : 'Generate Insights'}
							</button>
						</div>
					</form>
				</div>

				{error && <ErrorMessage message={error} />}
				{insight && <InsightResultDisplay insightText={insight} />}
			</div>
		</div>
	);
};

export default App;