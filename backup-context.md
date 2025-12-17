## Backup Context

- **AI Readiness:** 100%
- **Last Updated:** 2025-12-16

### Change Log
- 2025-12-15: Created GitHub Pages-ready site for Time Series Analysis and Forecasting using `Syllabus_alt.md` content; added `index.html`, `style.css`, and `README.md`; initialized this backup log.
- 2025-12-15: Added light/dark theme toggle with stored preference; updated README note.
- 2025-12-15: Defaulted site to light theme and aligned all panels/backgrounds with theme variables.
- 2025-12-15: Applied theme colors to header/nav and replaced hero image with `mainpage_img.jpeg`.
- 2025-12-15: Swapped hero image to `bg2.jpeg` for light-mode header consistency.
- 2025-12-15: Added lecture/lab row highlighting in the teaching plan schedule.
- 2025-12-15: Increased contrast between lecture and lab week rows for clearer distinction.
- 2025-12-15: Backup context refreshed (no additional content changes).
- 2025-12-16: Fixed Springer LNCS LaTeX template (`samplepaper.tex`) for local compilation:
  - Modified template to work without Ghostscript by commenting out EPS figure and providing PDF/PNG alternatives
  - Added comprehensive student-friendly comments and instructions throughout the template
  - Made ORCID IDs optional with clear examples
  - Added figure insertion instructions with multiple format options (PDF, PNG, EPS)
  - Created `COMPILATION_GUIDE.md` with detailed compilation instructions, troubleshooting tips, and customization guide
  - Verified successful compilation (PDF generated: 246KB, 2 pages)
- 2025-12-16: Reorganized LaTeX template to follow standard scientific paper structure:
  - Replaced generic "First Section" with standard sections: Introduction, Related Work, Methodology, Experiments and Results, Discussion, Conclusion
  - Added detailed comments in each section explaining what content should be included
  - Organized subsections appropriately (e.g., "Previous Approaches", "Research Gaps" in Related Work; "Problem Formulation", "Proposed Approach" in Methodology)
  - Moved figure insertion instructions to Results section where they're more relevant
  - Added example content and structure guidance for each section
  - Verified successful compilation (PDF generated: 243KB, 4 pages)
- 2025-12-16: Updated LaTeX template for student use:
  - Modified ORCID instructions to use Student ID instead (format: \orcidID{StudentID})
  - Replaced manual bibliography with BibTeX setup using `references.bib` file
  - Created sample `references.bib` file with example entries (article, inproceedings, book, misc)
  - Updated compilation instructions to include BibTeX workflow (pdflatex -> bibtex -> pdflatex -> pdflatex)
  - Verified successful compilation with BibTeX (PDF generated: 323KB, 4 pages)
- 2025-12-16: Updated affiliation information:
  - Set all authors to belong to "Faculty of Data Science and Artificial Intelligence, College of Technology, National Economics University"
  - Updated author entries to use single institution (\inst{1} for all authors)
  - Added email placeholder with @neu.edu.vn domain
  - Verified successful compilation
- 2025-12-16: Added Author Contributions section:
  - Added Author Contributions subsection within the credits environment
  - Included CRediT (Contributor Roles Taxonomy) format with comprehensive role descriptions
  - Provided example contributions for three authors using CRediT taxonomy
  - Included alternative descriptive format (commented out) for reference
  - Placed before Acknowledgments section following standard scientific paper structure
  - Verified successful compilation
- 2025-12-16: Removed Acknowledgements and Disclosure of Interest sections:
  - Removed \ackname (Acknowledgements) subsection
  - Removed \discintname (Disclosure of Interest) subsection
  - Kept only Author Contributions section within credits environment
  - Verified successful compilation
- 2025-12-16: Personalized template with institutional logos:
  - Added NEU logo and FDA logo in the upper left corner of the title page
  - Copied logo files (NEU logo.png, FDA logo.png) to template directory
  - Positioned logos side by side in upper left corner using \vspace* and \noindent
  - Added float package for better figure placement control
  - Included comments with instructions for adjusting logo size and vertical positioning
  - Optimized spacing to keep logos, title, and abstract on one page:
    * Reduced logo size to 0.8cm
    * Added \enlargethispage{3cm} to increase first page space
    * Reduced spacing between elements
    * Added negative spacing after \maketitle and abstract
  - Modified llncs.cls file to fix page break issue:
    * Commented out \newpage commands in \maketitle (line 923) and \@maketitle (line 1006)
    * Commented out \newpage in single-column branch (line 943)
    * This allows logos, title, and abstract to appear on the same page
  - Verified successful compilation (PDF generated: 897KB, 4 pages - reduced from 5 pages)
- 2025-12-16: Created Overleaf-ready zip package:
  - Created `FDA_pp_template.zip` with only necessary files for compilation
  - Included files: samplepaper.tex, llncs.cls, references.bib, splncs04.bst, NEU logo.png, FDA logo.png, sample_method_fig.png
  - Excluded compilation artifacts (.aux, .log, .bbl, .blg, etc.) and documentation files
  - Files are at root level (no subdirectories) for easy Overleaf upload
  - Zip file size: 906KB, contains 7 essential files
- 2025-12-16: Fixed LaTeX poster template (PosterSIFISC) for compilation:
  - Added missing packages: `url` (for \url command) and `subcaption` (for subfigure support)
  - Fixed subfigure syntax in `Seções/Resultados.tex` to use modern `subcaption` package instead of deprecated `subfig`
  - Added compilation instructions in `main.tex` about sciposter class requirement
  - Created `COMPILATION_GUIDE.md` with detailed instructions for Overleaf and local compilation
  - Template requires `sciposter` class (available in Overleaf, needs installation for local use)
  - All syntax errors fixed; template ready for Overleaf compilation
- 2025-12-16: Fixed Overleaf compilation issues for poster template:
  - Added Overleaf magic comments (`% !TeX program = pdflatex`) to main.tex
  - Fixed `\url` command inside TikZ node (changed to `\texttt` to avoid conflicts)
  - Created `OVERLEAF_SETUP.md` with step-by-step Overleaf setup instructions
  - Added troubleshooting guide for "Recipe terminated with error" issues
  - Instructions for setting main document and compiler in Overleaf
- 2025-12-16: Fixed latexmk cached error issue for poster template:
  - Created `clean.sh` script to remove LaTeX compilation artifacts
  - Created `.latexmkrc` configuration file for proper latexmk behavior
  - Updated `COMPILATION_GUIDE.md` with troubleshooting for "gave an error in previous invocation" messages
  - Solution: Run `./clean.sh` or manually remove .aux, .log files to clear cached errors
  - Updated `clean.sh` to also remove PDF file (latexmk caches based on PDF existence)
  - Created `README.md` with quick start guide and troubleshooting
  - Updated `.latexmkrc` with better error handling configuration
  - Key fix: Must remove `main.pdf` to clear cached errors, not just auxiliary files
- 2025-12-16: Fixed subfigure conflict in poster template:
  - Removed `subcaption` package (conflicts with sciposter's built-in `\subfigure` command)
  - Updated `Seções/Resultados.tex` to use sciposter's native `\subfigure` syntax instead of subcaption environment
  - sciposter class provides its own `\subfigure` command, so subcaption package is not needed
  - Verified successful compilation (PDF generated: 666KB, 1 page)
- 2025-12-16: Fixed header alignment and standardized language to English for poster template:
  - Fixed header alignment in `preposterTikz.sty`:
    * Changed title node positioning from fixed coordinates to centered with text width constraints
    * Added `text width=0.7\paperwidth` and `align=center` to all header nodes for proper centering
    * Adjusted vertical spacing and node distances for better alignment
  - Standardized all text to English:
    * Changed babel package from `brazil` to `english` in `preposterTikz.sty`
    * Converted all section titles: RESUMO→ABSTRACT, OBJETIVOS→OBJECTIVES, METODOLOGIA→METHODOLOGY, RESULTADOS→RESULTS, CONCLUSÕES→CONCLUSIONS, REFERÊNCIAS→REFERENCES, APOIADORES→ACKNOWLEDGMENTS
    * Replaced all Portuguese placeholder text with English placeholder text in all section files
    * Updated all comments from Portuguese to English throughout `main.tex` and `preposterTikz.sty`
    * Changed example text in sections to professional English placeholder content
    * Updated theorem environment labels: Exemplo→Example, Definição→Definition
    * Updated footer URL placeholder to generic example.com
  - All files now use English language and professional placeholder text
- 2025-12-16: Fixed "Recipe terminated with error" issue in poster template:
  - Fixed `.latexmkrc` configuration file:
    * Removed `$max_repeat = 0;` which was preventing latexmk from running multiple passes
    * Now uses default max_repeat (5 passes) for proper reference resolution
    * Added `$bibtex_use = 0;` and `$biber_use = 0;` to disable bibliography processing (not used in this template)
    * Improved error handling configuration
  - The issue was that latexmk couldn't complete compilation because it was limited to 0 passes
  - Verified successful compilation with latexmk (PDF generated: 661KB, 2 pages)
- 2025-12-16: Removed acknowledgments section from poster template:
  - Removed `\input{Seções/Apoiadores}` from `main.tex`
  - The acknowledgments section (ACKNOWLEDGMENTS) is no longer included in the poster
  - The `Seções/Apoiadores.tex` file still exists but is not used
- 2025-12-16: Fixed header alignment in poster template:
  - Adjusted title and author positioning in `preposterTikz.sty`:
    * Changed vertical positioning from fixed `-3.8cm` to `-0.5*\altura` to center content vertically within the header
    * Increased text width from `0.75\paperwidth` to `0.8\paperwidth` for better spacing
    * Used `anchor=center` and `x=0` positioning to ensure perfect horizontal centering
    * Title and author information now properly centered both horizontally and vertically within the header bar
  - Verified successful compilation (PDF generated: 536KB)
- 2025-12-16: Replaced complex TikZ header with simple plain header in poster template:
  - Removed complex TikZ-based header with multiple overlays and positioning
  - Created simple header using `\colorbox` and `\parbox` for plain formatting
  - Header now uses simple centered text layout with colored background
  - Removed logo positioning complexity - header is now text-only
  - Simplified `\titulo` command to use basic LaTeX formatting
  - Header displays title, subtitle, authors, and institution in a clean, centered format
  - Verified successful compilation
- 2025-12-16: Standardized poster template format to match Springer LNCS style:
  - Updated author format to Springer LNCS style:
    * Changed from simple format to `First Author\inst{1}\orcidID{StudentID} \and Second Author\inst{1}\orcidID{StudentID}`
    * Added `\inst` command for institution superscripts
    * Added `\orcidID` command (using Student ID for students, displays as "ID: 20201234")
    * Updated institution format to match Springer style with `\email` command
    * Fixed `\and` separator handling in header to display multiple authors correctly
  - Updated figure format to Springer LNCS style:
    * Changed to `\begin{figure}\centering\includegraphics[...]\caption{...}\label{...}\end{figure}`
    * Added figure references using `Figure~\ref{fig:label}`
    * Maintained support for subfigures using sciposter's `\subfigure` command
  - Updated table format to Springer LNCS style:
    * Changed to `\begin{table}\caption{...}\label{...}\centering\begin{tabular}...\end{tabular}\end{table}`
    * Added table references using `Table~\ref{tab:label}`
    * Matched Springer table structure and formatting
  - All formats now consistent with Springer LNCS paper template
  - Verified successful compilation (PDF generated: 144KB, 2 pages)
- 2025-12-16: Updated poster template sections - moved figure to Methodology, removed from Results:
  - Removed all figures from Results section:
    * Removed single figure (fig:example1) showing experimental results
    * Removed subfigures (fig:example2) showing comparison of experimental conditions
    * Kept only the table (tab1) for presenting comparison of different methods
    * Updated section text to focus on tables and descriptive text
  - Added methodology figure to Methodology section:
    * Copied `sample_method_fig.png` from Springer template to `Figuras/` directory
    * Added figure using Springer LNCS style format: `\begin{figure}\centering\includegraphics[...]\caption{...}\label{fig:method}\end{figure}`
    * Figure shows "Overview of the proposed method architecture and workflow"
    * Added figure reference: `Figure~\ref{fig:method}`
    * Positioned figure before the methodology description text
  - Verified successful compilation (PDF generated: 133KB, 2 pages)
- 2025-12-16: Cleaned and standardized PosterSIFISC template file names to English:
  - Removed all compilation artifacts (.aux, .log, .pdf, .fdb_latexmk, .fls, .synctex.gz)
  - Removed documentation files (README.md, COMPILATION_GUIDE.md, OVERLEAF_SETUP.md, INSTALL_SCIPOSTER.md)
  - Removed scripts (clean.sh, INSTALL_PACKAGES.sh, .latexmkrc)
  - Renamed directory "Seções" → "Sections"
  - Renamed section files to English:
    * Resumo.tex → Abstract.tex
    * Objetivos.tex → Objectives.tex
    * Metodologia.tex → Methodology.tex
    * Resultados.tex → Results.tex
    * Conclusões.tex → Conclusions.tex
    * Referências.tex → References.tex
    * Removed Apoiadores.tex (not used)
  - Renamed directory "Figuras" → "Figures"
  - Updated all file paths in main.tex and section files
  - Updated graphicspath in preposterTikz.sty to use "Figures"
  - Template now contains only necessary files for compilation
  - Verified successful compilation (PDF generated: 133KB, 2 pages)
- 2025-12-16: Added FDA logo to poster header:
  - Copied FDA logo.png from Springer template to poster template directory
  - Modified header in preposterTikz.sty to include FDA logo in upper left corner
  - Logo positioned at height 1.2cm with proper spacing
  - Logo appears in the colored header box above the title
  - Verified successful compilation (PDF generated: 617KB, 2 pages - size increased due to logo inclusion)
- 2025-12-16: Removed Class Regulations section and added Topics page to website:
  - Removed "Class Regulations" section from main index.html
  - Added "Topics" link to navigation menu
  - Created new topics.html page displaying all 14 project topics
  - Topics page features:
    * Visual grid layout with topic cards
    * Featured images from each topic folder (14 .jpeg files)
    * Difficulty level badges (Easy, Medium, Hard)
    * Bonus points indicator (+5 points for Hard topics)
    * Difficulty legend explaining levels and bonus system
    * Topic metadata (domain, data frequency)
    * Responsive design matching main page color theme
    * Hover effects and smooth transitions
  - All topic images properly linked and displayed
  - Maintains consistent styling with main page (light/dark theme support)
  - Created folders in `Topic/` directory for all 14 topics from `Topic_notes.md`:
    * 1.SP_500 - Basic Stock Price Time Series (S&P 500)
    * 2.Business_Sales - Monthly Business Sales Time Series
    * 3.GDP - GDP Time Series for Multiple Countries
    * 4.US_Macro - US Macroeconomic Indicators
    * 5.NVIDIA_Stock - Single-Stock Case Study: NVIDIA
    * 6.Multivariate_Financial - Multivariate Financial Time Series Bundle
    * 7.Human_Vital_Signs - Human Vital Signs (Kaggle)
    * 8.VitalDB - High-Resolution Vital Signs with VitalDB
    * 9.Airline_Passengers - Airline Passenger Time Series (Statsmodels)
    * 10.EEG_MNE - EEG Analysis with MNE Sample Dataset
    * 11.ECG_MIT_BIH - ECG Analysis with MIT-BIH (WFDB)
    * 12.Open_Time_Series - Open Multidomain Time Series
    * 13.Store_Sales - Retail Store Sales Time Series (Kaggle Competition)
    * 14.Electricity_Load - Electricity Load Diagrams
  - Each folder contains a comprehensive README.md with:
    * Dataset information and download instructions
    * Data loading code examples
    * Step-by-step implementation guide (EDA, preprocessing, modeling, evaluation)
    * Expected deliverables
    * Tips and best practices
    * Domain-specific considerations
  - README files are based on content from `Topic_notes.md` and provide detailed guidance for students implementing each topic
  - Created starter Jupyter notebooks (`starter.ipynb`) for all 14 topics:
    * Each notebook includes installation instructions for required packages
    * Data loading code with examples adapted from `Topic_notes.md`
    * Basic data exploration cells (shape, columns, missing values, statistics)
    * Initial visualization cells for time series plotting
    * Notebooks are ready-to-use templates that students can build upon
    * Special handling for library-based datasets (VitalDB, MNE, WFDB, statsmodels)

