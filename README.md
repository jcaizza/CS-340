# CS-340 – Project Two Reflection

## 1) Writing programs that are maintainable, readable, and adaptable

**How do you write programs that are maintainable, readable, and adaptable?**  
I keep the code in small parts that each do one clear job. All database work lives in one file (`animal_shelter.py`) with simple functions like create, read, update, and delete. The dashboard calls those functions instead of talking to the database directly. I use clear names, short functions, and a few comments so someone new can follow the flow. Settings like the database URL are not hard-coded, so I can switch environments without changing the code.

**What were the advantages of working in this way?**  
It made changes fast and safe. If I needed to fix or improve a query, I only changed it in one place. The dashboard stayed clean because it didn’t contain database details. Testing was easier because I could run the CRUD functions by themselves. This also reduced repeated code and lowered the chance of bugs.

**How else could you use this CRUD Python module in the future?**  
I can reuse the same module in many places: a small web app, a command-line script, a scheduled job that runs reports, or another dashboard. Most of the time, I would only update the connection settings or add one new function, instead of rebuilding everything from scratch.

---

## 2) Approach to problems as a computer scientist

**How do you approach a problem as a computer scientist?**  
I start by asking, “What does the user need to see or do?” Then I break that goal into small steps: what data is needed, how to filter it, and what result should show on screen. I test small queries first to be sure they work, then connect them to the dashboard. I keep the code simple and improve it as I learn more.

**How did your approach to this project differ from previous assignments in other courses?**  
I focused more on doing work inside the database (filtering, sorting, and counting there), so less data had to move into Python. I also put all data access in one module and kept the dashboard just for display and user actions. This made the project feel closer to real client work.

**What techniques or strategies would you use in the future to create databases to meet other client requests?**  
I would gather clear requirements first, design the data to match those needs, and plan the most common searches up front. I would return only the fields the screen needs, add indexes for the heavy searches, handle “no results” nicely, and write short notes in the code so others can maintain it. I would also test with sample data early to catch slow or confusing steps.

---

## 3) What computer scientists do and why it matters

**What do computer scientists do, and why does it matter?**  
They turn real-world needs into tools that save time and reduce mistakes. Good tools make information easy to find, easy to trust, and easy to act on.

**How would your work on this type of project help a company like Grazioso Salvare?**  
The dashboard lets staff quickly find the right animals, update records in one place, and see clear summaries without digging through spreadsheets. That means faster decisions, fewer errors, and more time focused on their mission instead of wrestling with data.
