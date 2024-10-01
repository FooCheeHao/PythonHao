# CNN Selenium NewsScraper

## Project Overview
This is a Selenium-based web scraping project used to scrape news from the CNN website, save it as a CSV file, and generate a detailed report. The project includes the following three files:

1. `cnnnews.py`: The source code of the Selenium web scraper.
2. `cnnnews.csv`: The records of the news captured by the scraper, saved in CSV format.
3. `report.docx`: A detailed report generated based on the scraper results.

## File Descriptions

### 1. `cnnnews.py`
This is the core Python script of the project, which uses Selenium to automate browser operations to scrape news data from the CNN website. The script includes the following features:
- Automatically opens the browser and visits CNN's news page
- Retrieves the latest news titles
- Saves this information to a CSV file

### 2. `cnnnews.csv`
This is the output file generated after running the Selenium scraper. It contains the titles of CNN news articles scraped from each page.

### 3. `report.docx`
This is a detailed report generated based on the `cnnnews.csv` file, which includes news statistics and analysis. This file can be opened with Microsoft Word or any other software that supports the .docx format.

## Usage Instructions
- Make sure you have installed Python and the required dependencies.
- Download the appropriate browser driver and configure the path.
- Run `cnnnews.py` to scrape news data from the CNN website.
- Check the generated `cnnnews.csv` file.
- For detailed analysis, view the `report.docx`.
