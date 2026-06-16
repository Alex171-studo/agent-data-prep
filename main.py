from src.loader import load_all
from src.cleaner import clean_all
from src.analyzer import analyze_all,print_results
from src.exporter import export_all, export_analysis
from src.summarizer import summarize_for_agent, save_summary

datasets = load_all()
cleaned = clean_all(datasets)
results = analyze_all(cleaned)
print_results(results)
export_all(cleaned)
export_analysis(results)

summary = summarize_for_agent(cleaned,results)
print(summary)
save_summary(summary)