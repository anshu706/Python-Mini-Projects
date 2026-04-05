const APP_META = [
        {
          id: "atm",
          icon: "[ATM]",
          name: "ANTEIKU ATM",
          sub: "Banking Simulator",
          color: "#2ec8ff",
          tag: "BANKING",
        },
        {
          id: "library",
          icon: "[LIB]",
          name: "Neo Library",
          sub: "Book Management",
          color: "#00d084",
          tag: "MGMT",
        },
        {
          id: "periodic",
          icon: "[CHEM]",
          name: "Periodic Table",
          sub: "118 Elements Explorer",
          color: "#c77dff",
          tag: "SCIENCE",
        },
        {
          id: "phonebook",
          icon: "[PB]",
          name: "Modern Phonebook",
          sub: "Contact Manager",
          color: "#86e1fc",
          tag: "CONTACTS",
        },
        {
          id: "quiz",
          icon: "[QUIZ]",
          name: "Knowledge Arena",
          sub: "Tech Trivia Quiz",
          color: "#cba6f7",
          tag: "GAME",
        },
        {
          id: "billing",
          icon: "[BILL]",
          name: "Smart Billing",
          sub: "Boutique POS Desk",
          color: "#ffbe0b",
          tag: "RETAIL",
        },
        {
          id: "casino",
          icon: "[CAS]",
          name: "Lucky Casino",
          sub: "Number Guess Game",
          color: "#ff006e",
          tag: "GAME",
        },
        {
          id: "guess",
          icon: "[GUESS]",
          name: "Mystery Number",
          sub: "Guess in 3 Tries",
          color: "#00ff88",
          tag: "PUZZLE",
        },
      ];

      const state = {
        current: null,
        atmAccounts: [
          {
            card_code: "k",
            name: "Ken Kaneki",
            title: "Midnight Account",
            pin: 1234,
            balance: 50000,
          },
          {
            card_code: "s",
            name: "Sasuke Uchiha",
            title: "Storm Account",
            pin: 5678,
            balance: 100000,
          },
          {
            card_code: "i",
            name: "Itachi Uchiha",
            title: "Shadow Account",
            pin: 9123,
            balance: 60000,
          },
          {
            card_code: "l",
            name: "Light Yagami",
            title: "Nova Account",
            pin: 8123,
            balance: 40000,
          },
        ],
        atmSelected: null,
        atmUnlocked: false,
        atmAttempts: 0,

        libraryBooks: [
          {
            title: "Introduction to C",
            author: "Dennis Ritchie",
            pages: 280,
            price: 350,
            code: 123,
            stock: 2,
          },
          {
            title: "Introduction to Python",
            author: "Guido Rossum",
            pages: 320,
            price: 420,
            code: 456,
            stock: 3,
          },
          {
            title: "Fundamentals of Thermodynamics",
            author: "Moran",
            pages: 510,
            price: 670,
            code: 153,
            stock: 13,
          },
        ],

        phoneContacts: [],
        phoneFilter: "",
        phoneSelected: null,

        quiz: {
          questions: [
            {
              q: "Which was the first search engine on the internet?",
              opts: ["Google", "Archie", "Wais", "Altavista"],
              ans: 1,
            },
            {
              q: "Which browser was invented in 1990?",
              opts: ["Internet Explorer", "Mosaic", "Mozilla", "Nexus"],
              ans: 3,
            },
            {
              q: "The first computer virus is known as?",
              opts: ["Rabbit", "Creeper virus", "Elk Cloner", "SCA virus"],
              ans: 1,
            },
            {
              q: "Firewall in a computer is used for?",
              opts: [
                "Security",
                "Data Transmission",
                "Monitoring",
                "Authentication",
              ],
              ans: 0,
            },
            {
              q: "Which one is NOT a database software?",
              opts: ["MySQL", "Oracle", "COBOL", "Sybase"],
              ans: 2,
            },
          ],
          qi: 0,
          score: 0,
          selected: -1,
          status: "Ready to begin",
        },

        billingPrices: {
          Cosmetics: {
            "Body Soap": 10,
            "Hair Cream": 25,
            "Hair Spray": 50,
            "Body Spray": 50,
          },
          Grocery: { Sugar: 100, Tea: 15, Coffee: 50, Rice: 150, Wheat: 160 },
          Beverages: {
            Pepsi: 30,
            Sprite: 35,
            Coke: 30,
            Mojitos: 25,
            "Thumbs Up": 35,
          },
        },
        billingQty: {},

        casino: {
          started: false,
          player: "",
          balance: 0,
        },

        guess: {
          secret: 1 + Math.floor(Math.random() * 10),
          lives: 3,
          count: 0,
          over: false,
          history: [],
        },
      };

      const CAT_COLORS = {
        nonmetal: "#e74c3c",
        noble_gas: "#9b59b6",
        alkali_metal: "#f39c12",
        alkaline_earth: "#d5a6bd",
        metalloid: "#95a5a6",
        transition_metal: "#3498db",
        lanthanide: "#1abc9c",
        metal: "#c0392b",
      };

      const ELEMENTS = (() => {
        const raw = [
          [1, "H", "Hydrogen", 1.008, "Gas", "nonmetal"],
          [2, "He", "Helium", 4.003, "Gas", "noble_gas"],
          [3, "Li", "Lithium", 6.941, "Solid", "alkali_metal"],
          [4, "Be", "Beryllium", 9.012, "Solid", "alkaline_earth"],
          [5, "B", "Boron", 10.811, "Solid", "metalloid"],
          [6, "C", "Carbon", 12.011, "Solid", "nonmetal"],
          [7, "N", "Nitrogen", 14.007, "Gas", "nonmetal"],
          [8, "O", "Oxygen", 15.999, "Gas", "nonmetal"],
          [9, "F", "Fluorine", 18.998, "Gas", "nonmetal"],
          [10, "Ne", "Neon", 20.18, "Gas", "noble_gas"],
          [11, "Na", "Sodium", 22.99, "Solid", "alkali_metal"],
          [12, "Mg", "Magnesium", 24.305, "Solid", "alkaline_earth"],
          [13, "Al", "Aluminium", 26.982, "Solid", "metal"],
          [14, "Si", "Silicon", 28.086, "Solid", "metalloid"],
          [15, "P", "Phosphorus", 30.974, "Solid", "nonmetal"],
          [16, "S", "Sulfur", 32.065, "Solid", "nonmetal"],
          [17, "Cl", "Chlorine", 35.453, "Gas", "nonmetal"],
          [18, "Ar", "Argon", 39.948, "Gas", "noble_gas"],
          [19, "K", "Potassium", 39.098, "Solid", "alkali_metal"],
          [20, "Ca", "Calcium", 40.078, "Solid", "alkaline_earth"],
          [26, "Fe", "Iron", 55.845, "Solid", "transition_metal"],
          [29, "Cu", "Copper", 63.546, "Solid", "transition_metal"],
          [47, "Ag", "Silver", 107.868, "Solid", "transition_metal"],
          [79, "Au", "Gold", 196.967, "Solid", "transition_metal"],
          [80, "Hg", "Mercury", 200.592, "Liquid", "transition_metal"],
          [92, "U", "Uranium", 238.029, "Solid", "lanthanide"],
        ];
        for (let i = 21; i < 26; i += 1)
          raw.push([
            i,
            `E${i}`,
            `Element-${i}`,
            i,
            "Solid",
            "transition_metal",
          ]);
        for (let i = 30; i < 47; i += 1)
          raw.push([
            i,
            `E${i}`,
            `Element-${i}`,
            i,
            "Solid",
            "transition_metal",
          ]);
        for (let i = 48; i < 79; i += 1)
          raw.push([
            i,
            `E${i}`,
            `Element-${i}`,
            i,
            "Solid",
            i < 72 ? "lanthanide" : "transition_metal",
          ]);
        for (let i = 81; i < 92; i += 1)
          raw.push([i, `E${i}`, `Element-${i}`, i, "Solid", "metal"]);
        for (let i = 93; i < 119; i += 1)
          raw.push([i, `E${i}`, `Element-${i}`, i, "Solid", "lanthanide"]);
        return raw
          .map((r) => ({
            n: r[0],
            sym: r[1],
            name: r[2],
            mass: r[3],
            state: r[4],
            cat: r[5],
          }))
          .sort((a, b) => a.n - b.n);
      })();

      const ELEM_FACTS = {
        1: "Most abundant element in the universe",
        6: "Forms diamond and graphite allotropes",
        7: "Essential for life and proteins",
        8: "Required for respiration",
        26: "Main component of Earth's core",
        79: "Most precious metal and resistant to corrosion",
        80: "Only metal liquid at room temperature",
        92: "Heaviest naturally occurring element",
      };

      function el(id) {
        return document.getElementById(id);
      }

      function esc(s) {
        return String(s)
          .replaceAll("&", "&amp;")
          .replaceAll("<", "&lt;")
          .replaceAll(">", "&gt;")
          .replaceAll('"', "&quot;");
      }

      function setTop(meta) {
        const crumb = el("breadcrumb");
        const badge = el("badge");
        if (!meta) {
          crumb.textContent = "mini_py / Home";
          badge.style.visibility = "hidden";
          return;
        }
        crumb.textContent = `mini_py / ${meta.name}`;
        badge.textContent = meta.tag;
        badge.style.background = meta.color;
        badge.style.visibility = "visible";
      }

      function setActiveNav(id) {
        document.querySelectorAll(".nav-btn[data-id]").forEach((b) => {
          b.classList.toggle("active", b.dataset.id === id);
        });
      }

      function initNav() {
        const nav = el("navList");
        nav.innerHTML = APP_META.map(
          (m) =>
            `<button class="nav-btn" data-id="${m.id}">${m.icon} ${esc(m.name)}</button>`,
        ).join("");

        nav.querySelectorAll("button").forEach((btn) => {
          btn.addEventListener("click", () => launch(btn.dataset.id));
        });

        el("homeBtn").addEventListener("click", showHome);
      }

      function showHome() {
        state.current = null;
        setTop(null);
        setActiveNav(null);
        const main = el("main");
        main.innerHTML = `
        <section class="home-hero">
          <span class="pill"> Python Mini Projects Collection</span>
          <h1 class="title-xl">mini_py</h1>
          <p class="muted">Eight complete mini apps. One launcher. Click any card to run.</p>
          <div class="stats">
            <div><div class="stat-num">8</div><div class="stat-lbl">Apps</div></div>
            <div><div class="stat-num">3k+</div><div class="stat-lbl">Lines (original)</div></div>
            <div><div class="stat-num">1</div><div class="stat-lbl">Browser File</div></div>
          </div>
        </section>
        <section class="cards-grid" id="homeCards"></section>
      `;

        const cards = el("homeCards");
        cards.innerHTML = APP_META.map(
          (m) => `
        <article class="app-card">
          <div>
            <div class="stripe" style="background:${m.color}"></div>
            <div class="row">
              <div style="font-size:24px;">${m.icon}</div>
              <span class="tag">${m.tag}</span>
            </div>
            <div style="margin-top:8px;font-weight:700;">${esc(m.name)}</div>
            <div class="small" style="margin-top:4px;">${esc(m.sub)}</div>
          </div>
          <button class="launch-btn" style="background:${m.color};" data-id="${m.id}"> Launch</button>
        </article>
      `,
        ).join("");

        cards.querySelectorAll(".launch-btn").forEach((b) => {
          b.addEventListener("click", () => launch(b.dataset.id));
        });
      }

      function launch(id) {
        const meta = APP_META.find((m) => m.id === id);
        if (!meta) return;
        state.current = id;
        setTop(meta);
        setActiveNav(id);

        if (id === "atm") return renderATM();
        if (id === "library") return renderLibrary();
        if (id === "periodic") return renderPeriodic();
        if (id === "phonebook") return renderPhonebook();
        if (id === "quiz") return renderQuiz();
        if (id === "billing") return renderBilling();
        if (id === "casino") return renderCasino();
        if (id === "guess") return renderGuess();
      }

      function renderATM() {
        const main = el("main");
        main.innerHTML = `
        <div class="split">
          <section class="panel vstack">
            <h2 style="margin:0;color:#2ec8ff;">ANTEIKU ATM v3</h2>
            <div class="small">Select an account card and unlock with PIN.</div>
            <div id="atmCards" class="hstack"></div>
            <div class="panel" style="background:#0f1630;">
              <div style="font-weight:700;">PIN Verification</div>
              <div class="small" id="atmPinHint">Select an account first</div>
              <div class="hstack" style="margin-top:8px;">
                <input id="atmPin" class="input" maxlength="4" placeholder="4-digit PIN" style="max-width:180px;" />
                <button id="atmUnlock" class="btn" style="background:#48f0b8;color:#06221c;font-weight:700;">Unlock</button>
              </div>
            </div>
          </section>

          <section class="panel vstack">
            <div style="font-weight:700;">Session Actions</div>
            <div class="small" id="atmActive">No card inserted</div>
            <label class="small">Withdraw Amount</label>
            <input id="atmWd" class="input" placeholder="e.g. 2000" />
            <button id="atmBalBtn" class="btn" style="background:#37a5ff;color:#041428;font-weight:700;">Check Balance</button>
            <button id="atmWdBtn" class="btn" style="background:#ff5588;color:#1d0016;font-weight:700;">Withdraw Cash</button>
            <div id="atmStatus" class="status">Insert a card to begin.</div>
            <textarea id="atmReceipt" class="textarea" readonly></textarea>
          </section>
        </div>
      `;

        const cards = el("atmCards");
        cards.innerHTML = state.atmAccounts
          .map(
            (a) =>
              `<button class="btn" data-code="${a.card_code}" style="background:#15284f;color:#eef2ff;border:1px solid #2a3f6a;text-align:left;min-width:180px;">
          <div style="font-weight:700;">${esc(a.name)}</div>
          <div class="small">${esc(a.title)} | ${a.card_code.toUpperCase()}</div>
        </button>`,
          )
          .join("");

        const status = el("atmStatus");
        const receipt = el("atmReceipt");
        const active = el("atmActive");
        const pinHint = el("atmPinHint");

        function writeReceipt(lines) {
          receipt.value = lines.join("\n");
        }

        function setButtons(enabled) {
          el("atmBalBtn").disabled = !enabled;
          el("atmWdBtn").disabled = !enabled;
        }

        setButtons(false);
        writeReceipt(["-- ANTEIKU ATM --", "Insert a card to begin."]);

        cards.querySelectorAll("button").forEach((b) => {
          b.addEventListener("click", () => {
            const acc = state.atmAccounts.find(
              (x) => x.card_code === b.dataset.code,
            );
            state.atmSelected = acc || null;
            state.atmUnlocked = false;
            state.atmAttempts = 0;
            el("atmPin").value = "";
            el("atmWd").value = "";
            cards.querySelectorAll("button").forEach((x) => {
              x.style.background = x === b ? "#1d3f75" : "#15284f";
            });
            if (!acc) return;
            active.textContent = `Active: ${acc.name}`;
            pinHint.textContent = "Enter PIN and press Unlock";
            status.textContent = `Card inserted: ${acc.name}\nPIN attempts left: 3`;
            writeReceipt([
              "-- ANTEIKU ATM --",
              `USER   : ${acc.name}`,
              `ACCT   : ${acc.title}`,
              "STATUS : Card inserted",
              "",
              "Authenticate to continue.",
            ]);
            setButtons(false);
          });
        });

        el("atmUnlock").addEventListener("click", () => {
          const acc = state.atmSelected;
          if (!acc) {
            status.textContent = "Select an account card first.";
            return;
          }
          const pin = el("atmPin").value.trim();
          if (!/^\d{4}$/.test(pin)) {
            status.textContent = "PIN must be exactly 4 digits.";
            return;
          }
          if (Number(pin) === acc.pin) {
            state.atmUnlocked = true;
            pinHint.textContent = "Session unlocked";
            status.textContent = `Access granted: ${acc.name}\nYou may check balance or withdraw.`;
            setButtons(true);
            return;
          }
          state.atmAttempts += 1;
          const left = 3 - state.atmAttempts;
          el("atmPin").value = "";
          if (left <= 0) {
            state.atmSelected = null;
            state.atmUnlocked = false;
            setButtons(false);
            active.textContent = "No card inserted";
            pinHint.textContent = "Session blocked. Re-insert card.";
            status.textContent = "PIN mismatch x3. Session blocked.";
            writeReceipt([
              "-- SECURITY --",
              "AUTH FAILED",
              "3 wrong PINs",
              "Re-insert card.",
            ]);
            cards.querySelectorAll("button").forEach((x) => {
              x.style.background = "#15284f";
            });
            return;
          }
          status.textContent = `PIN mismatch. Attempts left: ${left}`;
        });

        el("atmBalBtn").addEventListener("click", () => {
          const acc = state.atmSelected;
          if (!acc) {
            status.textContent = "Insert a card first.";
            return;
          }
          if (!state.atmUnlocked) {
            status.textContent = "Unlock session with PIN first.";
            return;
          }
          status.textContent = `Balance: ${acc.balance}`;
          writeReceipt([
            "-- BALANCE --",
            `USER    : ${acc.name}`,
            `BALANCE : ${acc.balance}`,
            "",
            "Thank you.",
          ]);
        });

        el("atmWdBtn").addEventListener("click", () => {
          const acc = state.atmSelected;
          if (!acc) {
            status.textContent = "Insert a card first.";
            return;
          }
          if (!state.atmUnlocked) {
            status.textContent = "Unlock session with PIN first.";
            return;
          }
          const text = el("atmWd").value.trim();
          if (!/^\d+$/.test(text)) {
            status.textContent = "Enter a valid numeric amount.";
            return;
          }
          const amt = Number(text);
          if (amt <= 0) {
            status.textContent = "Amount must be > 0.";
            return;
          }
          if (amt > acc.balance) {
            status.textContent = "Insufficient funds.";
            return;
          }
          acc.balance -= amt;
          status.textContent = `Dispensed: ${amt}\nRemaining: ${acc.balance}`;
          el("atmWd").value = "";
          writeReceipt([
            "-- RECEIPT --",
            `USER      : ${acc.name}`,
            `WITHDRAWN : ${amt}`,
            `REMAINING : ${acc.balance}`,
            "",
            "Collect cash safely.",
          ]);
        });
      }

      function renderLibrary() {
        const main = el("main");
        const books = state.libraryBooks;

        const totalStock = books.reduce((a, b) => a + b.stock, 0);
        const totalValue = books.reduce((a, b) => a + b.price * b.stock, 0);
        const avgPrice = books.length
          ? Math.floor(books.reduce((a, b) => a + b.price, 0) / books.length)
          : 0;

        main.innerHTML = `
        <div class="split">
          <section class="panel vstack">
            <h2 style="margin:0;color:#00d084;">Neo Library</h2>
            <div class="small">Catalog, search by code, add books, and quick stats.</div>
            <table>
              <thead>
                <tr><th>Code</th><th>Title</th><th>Author</th><th>Pages</th><th>Price</th><th>Stock</th></tr>
              </thead>
              <tbody>
                ${books.map((b) => `<tr><td>${b.code}</td><td>${esc(b.title)}</td><td>${esc(b.author)}</td><td>${b.pages}</td><td>Rs ${b.price}</td><td>${b.stock}</td></tr>`).join("")}
              </tbody>
            </table>
            <div class="small">Total: ${books.length} books | ${totalStock} units in stock</div>
          </section>

          <section class="panel vstack">
            <div class="kpi"><div class="small">Library Value</div><div class="n">Rs ${totalValue}</div></div>
            <div class="kpi"><div class="small">Avg Price</div><div class="n">Rs ${avgPrice}</div></div>

            <div class="panel" style="background:#0f1630;">
              <div style="font-weight:700;">Search by Code</div>
              <input id="libSearch" class="input" placeholder="Enter book code" style="margin-top:8px;" />
              <button id="libFind" class="btn" style="margin-top:8px;background:#00b8a9;color:#0d2818;font-weight:700;">Find</button>
              <div id="libSearchRes" class="status" style="margin-top:8px;"></div>
            </div>

            <div class="panel" style="background:#0f1630;">
              <div style="font-weight:700;">Add Book</div>
              <div class="vstack" style="margin-top:8px;">
                <input id="bTitle" class="input" placeholder="Title" />
                <input id="bAuthor" class="input" placeholder="Author" />
                <input id="bPages" class="input" placeholder="Pages" />
                <input id="bPrice" class="input" placeholder="Price" />
                <input id="bCode" class="input" placeholder="Code" />
                <input id="bStock" class="input" placeholder="Stock" />
              </div>
              <button id="libAdd" class="btn" style="margin-top:8px;background:#06ffa5;color:#05351f;font-weight:700;">Add to Library</button>
              <div id="libAddMsg" class="small" style="margin-top:6px;"></div>
            </div>
          </section>
        </div>
      `;

        el("libFind").addEventListener("click", () => {
          const t = el("libSearch").value.trim();
          const box = el("libSearchRes");
          if (!/^\d+$/.test(t)) {
            box.textContent = "Enter a valid number.";
            box.className = "status err";
            return;
          }
          const code = Number(t);
          const found = books.find((b) => b.code === code);
          if (!found) {
            box.textContent = `No book with code ${code}`;
            box.className = "status err";
            return;
          }
          box.textContent = `Found\nTitle: ${found.title}\nAuthor: ${found.author}\nPages: ${found.pages}\nPrice: Rs ${found.price}\nStock: ${found.stock}`;
          box.className = "status ok";
        });

        el("libAdd").addEventListener("click", () => {
          const msg = el("libAddMsg");
          const nb = {
            title: el("bTitle").value.trim(),
            author: el("bAuthor").value.trim(),
            pages: Number(el("bPages").value.trim()),
            price: Number(el("bPrice").value.trim()),
            code: Number(el("bCode").value.trim()),
            stock: Number(el("bStock").value.trim()),
          };

          if (!nb.title || !nb.author) {
            msg.textContent = "Title and Author are required.";
            msg.className = "small err";
            return;
          }
          if (
            [nb.pages, nb.price, nb.code, nb.stock].some(
              (x) => !Number.isFinite(x),
            )
          ) {
            msg.textContent =
              "Pages, Price, Code, and Stock must be valid numbers.";
            msg.className = "small err";
            return;
          }

          state.libraryBooks.push(nb);
          msg.textContent = "Book added successfully.";
          msg.className = "small ok";
          renderLibrary();
        });
      }

      function renderPeriodic() {
        const main = el("main");
        main.innerHTML = `
        <div class="split">
          <section class="panel vstack">
            <div class="hstack" style="justify-content:space-between;">
              <h2 style="margin:0;color:#ff6b35;">Periodic Table Explorer</h2>
              <div class="hstack">
                <button class="btn" data-cat="all">All</button>
                <button class="btn" data-cat="metal">Metals</button>
                <button class="btn" data-cat="nonmetal">Non-metals</button>
                <button class="btn" data-cat="noble_gas">Noble</button>
              </div>
            </div>
            <input id="elSearch" class="input" placeholder="Search by symbol, name, or number" />
            <div id="elGrid" class="periodic-grid"></div>
          </section>

          <section class="panel vstack">
            <div style="font-weight:700;color:#ff6b35;">Element Details</div>
            <textarea id="elDetail" class="textarea" readonly></textarea>
          </section>
        </div>
      `;

        const grid = el("elGrid");
        const detail = el("elDetail");
        let catFilter = "all";

        function renderGrid() {
          const q = el("elSearch").value.trim().toLowerCase();
          const rows = ELEMENTS.filter((e) => {
            const m1 = catFilter === "all" || e.cat === catFilter;
            const m2 =
              !q ||
              e.sym.toLowerCase().includes(q) ||
              e.name.toLowerCase().includes(q) ||
              String(e.n).includes(q);
            return m1 && m2;
          });

          grid.innerHTML = rows
            .map(
              (e) =>
                `<button class="el-btn" data-n="${e.n}" style="background:${CAT_COLORS[e.cat] || "#555"};">${e.sym}<br>${e.n}</button>`,
            )
            .join("");

          grid.querySelectorAll("button").forEach((b) => {
            b.addEventListener("click", () => {
              const n = Number(b.dataset.n);
              const item = ELEMENTS.find((x) => x.n === n);
              if (!item) return;
              const icon =
                item.state === "Gas"
                  ? ""
                  : item.state === "Liquid"
                    ? ""
                    : "";
              const fact =
                ELEM_FACTS[item.n] || "An important chemical element.";
              detail.value =
                `Element: ${item.name}\n` +
                `Symbol : ${item.sym}\n` +
                `Number : ${item.n}\n` +
                `Mass   : ${item.mass} u\n` +
                `State  : ${icon} ${item.state}\n` +
                `Cat    : ${item.cat.replaceAll("_", " ")}\n\n` +
                `Fact: ${fact}`;
            });
          });
        }

        detail.value = "Welcome. Click an element tile to see details.";

        el("elSearch").addEventListener("input", renderGrid);
        main.querySelectorAll("button[data-cat]").forEach((b) => {
          b.style.background = "#353535";
          b.style.color = "#fff";
          b.addEventListener("click", () => {
            catFilter = b.dataset.cat;
            renderGrid();
          });
        });

        renderGrid();
      }

      function renderPhonebook() {
        const main = el("main");
        const contacts = state.phoneContacts;
        const q = state.phoneFilter.trim().toLowerCase();
        const visible = contacts
          .map((c, i) => ({ c, i }))
          .filter(
            ({ c }) =>
              !q ||
              `${c.Name || ""} ${c.Phone || ""}`.toLowerCase().includes(q),
          );

        if (state.phoneSelected != null && !contacts[state.phoneSelected]) {
          state.phoneSelected = null;
        }

        main.innerHTML = `
        <div class="split-2">
          <section class="panel vstack">
            <h2 style="margin:0;color:#86e1fc;">Modern Phonebook</h2>
            <div class="hstack">
              <div class="kpi" style="flex:1;"><div class="small">Total</div><div class="n">${contacts.length}</div></div>
              <div class="kpi" style="flex:1;"><div class="small">Visible</div><div class="n">${visible.length}</div></div>
            </div>
            <input id="pbSearch" class="input" placeholder="Search by name or phone" value="${esc(state.phoneFilter)}" />
            <div id="pbList" class="list"></div>
            <button id="pbNew" class="btn" style="background:#7dc4e4;color:#10131e;font-weight:700;">+ Add Contact</button>
          </section>

          <section class="panel" id="pbRight"></section>
        </div>
      `;

        const list = el("pbList");
        if (!visible.length) {
          list.innerHTML = `<div class="small" style="padding:10px;">No contacts found.</div>`;
        } else {
          list.innerHTML = visible
            .map(
              ({ c, i }) =>
                `<button data-i="${i}" class="${state.phoneSelected === i ? "active" : ""}">${esc(c.Name || "?")}  ${esc(c.Phone || "")}</button>`,
            )
            .join("");
        }

        list.querySelectorAll("button").forEach((b) => {
          b.addEventListener("click", () => {
            state.phoneSelected = Number(b.dataset.i);
            renderPhonebook();
          });
        });

        const right = el("pbRight");
        const selected =
          state.phoneSelected == null ? null : contacts[state.phoneSelected];

        if (!selected) {
          right.innerHTML = `
          <div class="vstack" style="height:100%;justify-content:center;align-items:flex-start;">
            <div style="font-size:42px;"></div>
            <h3 style="margin:0;">No contact selected</h3>
            <div class="small">Add a contact or click a name from the list.</div>
            <button id="pbCreate" class="btn" style="background:#7dc4e4;color:#10131e;font-weight:700;">Create Contact</button>
          </div>
        `;
          right
            .querySelector("#pbCreate")
            .addEventListener("click", showPhoneCreate);
        } else {
          right.innerHTML = `
          <div class="vstack">
            <h3 style="margin:0;">${esc(selected.Name || "Unnamed")}</h3>
            <div style="font-size:20px;color:#7dc4e4;font-weight:700;">${esc(selected.Phone || "")}</div>
            <div class="panel" style="background:#121a2f;">
              <div><span class="small">Age: </span>${esc(selected.Age || "Not provided")}</div>
              <div><span class="small">DOB: </span>${esc(selected.DOB || "Not provided")}</div>
              <div><span class="small">Address: </span>${esc(selected.Address || "Not provided")}</div>
            </div>
            <button id="pbEdit" class="btn" style="background:#323a58;color:#eef2ff;">Add Another Contact</button>
          </div>
        `;
          right
            .querySelector("#pbEdit")
            .addEventListener("click", showPhoneCreate);
        }

        el("pbSearch").addEventListener("input", (e) => {
          state.phoneFilter = e.target.value;
          renderPhonebook();
        });

        el("pbNew").addEventListener("click", showPhoneCreate);
      }

      function showPhoneCreate() {
        const right = el("pbRight");
        if (!right) return;
        right.innerHTML = `
        <div class="vstack">
          <h3 style="margin:0;">Create Contact</h3>
          <input id="pcName" class="input" placeholder="Name" />
          <input id="pcPhone" class="input" placeholder="Phone" />
          <input id="pcAge" class="input" placeholder="Age" />
          <input id="pcDob" class="input" placeholder="DOB (DD-MM-YYYY)" />
          <input id="pcAddr" class="input" placeholder="Address" />
          <button id="pcSave" class="btn" style="background:#7dc4e4;color:#10131e;font-weight:700;">Save Contact</button>
          <div id="pcMsg" class="small"></div>
        </div>
      `;

        el("pcSave").addEventListener("click", () => {
          const d = {
            Name: el("pcName").value.trim(),
            Phone: el("pcPhone").value.trim(),
            Age: el("pcAge").value.trim(),
            DOB: el("pcDob").value.trim(),
            Address: el("pcAddr").value.trim(),
          };
          const msg = el("pcMsg");
          if (!d.Name || !d.Phone) {
            msg.textContent = "Name and Phone are required.";
            msg.className = "small err";
            return;
          }
          state.phoneContacts.push(d);
          state.phoneSelected = state.phoneContacts.length - 1;
          renderPhonebook();
        });
      }

      function renderQuiz() {
        const main = el("main");
        const qz = state.quiz;
        const total = qz.questions.length;

        const done = qz.qi >= total;
        const q = !done ? qz.questions[qz.qi] : null;
        const accuracy = total ? Math.round((qz.score / (total * 5)) * 100) : 0;

        main.innerHTML = `
        <div class="split">
          <section class="panel vstack">
            <h2 style="margin:0;color:#86e1fc;">Knowledge Arena</h2>
            <div class="hstack">
              <div class="kpi" style="flex:1;"><div class="small">Score</div><div class="n">${qz.score}</div></div>
              <div class="kpi" style="flex:1;"><div class="small">Question</div><div class="n">${Math.min(qz.qi + 1, total)} / ${total}</div></div>
            </div>
            <div class="status">${esc(qz.status)}</div>
            <div class="hstack">
              <button id="qStart" class="btn" style="background:#7dc4e4;color:#10131e;font-weight:700;">Start Quiz</button>
              <button id="qReset" class="btn" style="background:#323a58;color:#eef2ff;">Reset</button>
            </div>
          </section>

          <section class="panel" id="quizRight"></section>
        </div>
      `;

        const right = el("quizRight");
        if (done) {
          const verdict =
            qz.score >= 20
              ? "Elite run. You owned the arena."
              : qz.score >= 10
                ? "Strong session. Keep sharpening."
                : "Warm-up tier. Re-enter and try again.";

          right.innerHTML = `
          <div class="vstack">
            <h3 style="margin:0;color:#cba6f7;">Scoreboard</h3>
            <div style="font-size:32px;font-weight:700;">${qz.score} / ${total * 5}</div>
            <div class="small">Accuracy: ${accuracy}%</div>
            <div class="panel" style="background:#151e36;">${esc(verdict)}</div>
            <button id="qAgain" class="btn" style="background:#7dc4e4;color:#10131e;font-weight:700;">Play Again</button>
          </div>
        `;
          el("qAgain").addEventListener("click", quizStart);
        } else if (!q || qz.qi < 0) {
          right.innerHTML = `
          <div class="vstack">
            <h3 style="margin:0;">Ready to begin</h3>
            <div class="small">Press Start Quiz to begin the question set.</div>
          </div>
        `;
        } else {
          right.innerHTML = `
          <div class="vstack">
            <div class="small">Question ${qz.qi + 1}</div>
            <h3 style="margin:0;">${esc(q.q)}</h3>
            <div class="radio-wrap" id="qOpts"></div>
            <button id="qSubmit" class="btn" style="background:#7dc4e4;color:#10131e;font-weight:700;">Submit Answer</button>
          </div>
        `;

          const opts = el("qOpts");
          opts.innerHTML = q.opts
            .map(
              (o, i) =>
                `<label class="radio-card"><input type="radio" name="qopt" value="${i}" ${qz.selected === i ? "checked" : ""}/> ${esc(o)}</label>`,
            )
            .join("");

          opts.querySelectorAll("input").forEach((inp) => {
            inp.addEventListener("change", () => {
              qz.selected = Number(inp.value);
            });
          });

          el("qSubmit").addEventListener("click", () => {
            if (qz.selected === -1) {
              qz.status = "Pick an answer first!";
              renderQuiz();
              return;
            }
            if (qz.selected === q.ans) {
              qz.score += 5;
              qz.status = "Correct! +5 pts";
            } else {
              qz.status = `Wrong. Correct: option ${q.ans + 1}`;
            }
            qz.qi += 1;
            qz.selected = -1;
            renderQuiz();
          });
        }

        el("qStart").addEventListener("click", quizStart);
        el("qReset").addEventListener("click", quizReset);
      }

      function quizStart() {
        state.quiz.qi = 0;
        state.quiz.score = 0;
        state.quiz.selected = -1;
        state.quiz.status = "Question 1 - choose wisely.";
        renderQuiz();
      }

      function quizReset() {
        state.quiz.qi = -1;
        state.quiz.score = 0;
        state.quiz.selected = -1;
        state.quiz.status = "Session reset.";
        renderQuiz();
      }

      function renderBilling() {
        const main = el("main");
        const prices = state.billingPrices;

        for (const cat of Object.keys(prices)) {
          for (const item of Object.keys(prices[cat])) {
            const key = `${cat}::${item}`;
            if (!(key in state.billingQty)) state.billingQty[key] = 0;
          }
        }

        function totals() {
          const t = { Cosmetics: 0, Grocery: 0, Beverages: 0 };
          for (const cat of Object.keys(prices)) {
            for (const item of Object.keys(prices[cat])) {
              const q = Number(state.billingQty[`${cat}::${item}`]) || 0;
              t[cat] += prices[cat][item] * Math.max(0, q);
            }
          }
          return { ...t, Grand: t.Cosmetics + t.Grocery + t.Beverages };
        }

        const t = totals();

        main.innerHTML = `
        <div class="split">
          <section class="panel vstack">
            <h2 style="margin:0;color:#d7c4a6;">ANTEIKU SMART BILLING DESK</h2>
            <div class="small">Fill customer details, set quantities, then generate invoice.</div>
            <div class="hstack">
              <input id="billName" class="input" placeholder="Customer Name" />
              <input id="billPhone" class="input" placeholder="Phone" />
              <input id="billId" class="input" placeholder="Customer ID" />
            </div>

            <div class="panel" style="background:#121726;">
              <div style="font-weight:700;">Product Quantities</div>
              <div id="billItems" class="vstack" style="margin-top:10px;"></div>
            </div>

            <div class="hstack">
              <button id="billGen" class="btn" style="background:#6f3f2e;color:#fff2de;font-weight:700;">Generate Invoice</button>
              <button id="billClear" class="btn" style="background:#d7c4a6;color:#463533;">Clear All</button>
            </div>
            <div id="billStatus" class="small">Ready.</div>
          </section>

          <section class="panel vstack">
            <div class="kpi"><div class="small">Cosmetics</div><div class="n">Rs ${t.Cosmetics}</div></div>
            <div class="kpi"><div class="small">Grocery</div><div class="n">Rs ${t.Grocery}</div></div>
            <div class="kpi"><div class="small">Beverages</div><div class="n">Rs ${t.Beverages}</div></div>
            <div class="kpi"><div class="small">Grand Total</div><div class="n">Rs ${t.Grand}</div></div>
            <textarea id="billInvoice" class="textarea" readonly>ANTEIKU Billing\n--------------\nInvoice will appear here.</textarea>
          </section>
        </div>
      `;

        const wrap = el("billItems");
        wrap.innerHTML = Object.entries(prices)
          .map(
            ([cat, items]) =>
              `<div class="panel" style="background:#0f1630;">
          <div style="font-weight:700;margin-bottom:6px;">${cat}</div>
          ${Object.entries(items)
            .map(
              ([item, price]) =>
                `<div class="hstack" style="justify-content:space-between;margin-bottom:6px;">
              <div class="small">${esc(item)} (Rs ${price})</div>
              <input data-k="${cat}::${item}" type="number" min="0" value="${state.billingQty[`${cat}::${item}`] || 0}" class="input" style="max-width:90px;" />
            </div>`,
            )
            .join("")}
        </div>`,
          )
          .join("");

        wrap.querySelectorAll("input[data-k]").forEach((inp) => {
          inp.addEventListener("input", () => {
            state.billingQty[inp.dataset.k] = Math.max(
              0,
              Number(inp.value) || 0,
            );
            renderBilling();
          });
        });

        el("billGen").addEventListener("click", () => {
          const name = el("billName").value.trim() || "Walk-in Customer";
          const phone = el("billPhone").value.trim() || "N/A";
          const cid = el("billId").value.trim() || "N/A";
          const cur = totals();

          const lines = [
            "ANTEIKU SMART BILLING",
            "--------------------",
            `Customer : ${name}`,
            `Phone    : ${phone}`,
            `ID       : ${cid}`,
            "--------------------",
            "ITEMS",
          ];

          let any = false;
          for (const [cat, items] of Object.entries(prices)) {
            lines.push(`[${cat}]`);
            for (const [item, price] of Object.entries(items)) {
              const q = Math.max(
                0,
                Number(state.billingQty[`${cat}::${item}`]) || 0,
              );
              if (q > 0) {
                any = true;
                lines.push(
                  `${item.slice(0, 13).padEnd(13)} x${String(q).padEnd(2)} Rs ${price * q}`,
                );
              }
            }
          }

          if (!any) lines.push("No products selected");

          lines.push("--------------------");
          lines.push(`Cosmetics : Rs ${cur.Cosmetics}`);
          lines.push(`Grocery   : Rs ${cur.Grocery}`);
          lines.push(`Beverages : Rs ${cur.Beverages}`);
          lines.push(`Grand     : Rs ${cur.Grand}`);
          lines.push("--------------------");
          lines.push("Thank you!");

          el("billInvoice").value = lines.join("\n");
          el("billStatus").textContent = "Invoice generated successfully.";
        });

        el("billClear").addEventListener("click", () => {
          Object.keys(state.billingQty).forEach((k) => {
            state.billingQty[k] = 0;
          });
          renderBilling();
        });
      }

      function renderCasino() {
        const main = el("main");
        const c = state.casino;

        if (!c.started) {
          main.innerHTML = `
          <section class="panel vstack" style="max-width:760px;margin:0 auto;">
            <h2 style="margin:0;color:#ffbe0b;">Lucky Casino</h2>
            <div class="small">Guess a number from 1 to 10. Correct guess wins 10x your bet.</div>
            <input id="casName" class="input" placeholder="Player Name" />
            <input id="casDep" class="input" type="number" min="1" placeholder="Deposit Amount" />
            <button id="casStart" class="btn" style="background:#ff006e;color:#fff;font-weight:700;">Start Playing</button>
            <div id="casMsg" class="small"></div>
          </section>
        `;

          el("casStart").addEventListener("click", () => {
            const name = el("casName").value.trim();
            const dep = Number(el("casDep").value.trim());
            const msg = el("casMsg");
            if (!name) {
              msg.textContent = "Enter your name.";
              msg.className = "small err";
              return;
            }
            if (!Number.isFinite(dep) || dep <= 0) {
              msg.textContent = "Enter a valid deposit > 0.";
              msg.className = "small err";
              return;
            }
            c.player = name;
            c.balance = dep;
            c.started = true;
            renderCasino();
          });
          return;
        }

        main.innerHTML = `
        <section class="panel vstack" style="max-width:760px;margin:0 auto;">
          <div class="row">
            <div style="font-weight:700;"> ${esc(c.player)}</div>
            <div style="font-weight:700;color:#06ffa5;"> Balance: $${c.balance}</div>
          </div>
          <input id="casBet" class="input" type="number" min="1" value="10" placeholder="Bet Amount" />
          <label class="small">Pick a Number (1-10)</label>
          <div class="hstack" id="casNums"></div>
          <button id="casPlay" class="btn" style="background:#ff006e;color:#fff;font-weight:700;">Spin and Claim</button>
          <div id="casRes" class="status"></div>
          <button id="casQuit" class="btn" style="background:#323a58;color:#eef2ff;">Quit</button>
        </section>
      `;

        let picked = 1;
        const nums = el("casNums");
        nums.innerHTML = Array.from({ length: 10 }, (_, i) => i + 1)
          .map(
            (n) =>
              `<button class="btn" data-n="${n}" style="background:${n === 1 ? "#8338ec" : "#1a1a2e"};color:#fff;">${n}</button>`,
          )
          .join("");

        nums.querySelectorAll("button").forEach((b) => {
          b.addEventListener("click", () => {
            picked = Number(b.dataset.n);
            nums.querySelectorAll("button").forEach((x) => {
              x.style.background = x === b ? "#8338ec" : "#1a1a2e";
            });
          });
        });

        el("casPlay").addEventListener("click", () => {
          const bet = Number(el("casBet").value.trim());
          const res = el("casRes");
          if (!Number.isFinite(bet) || bet <= 0 || bet > c.balance) {
            res.textContent = `Invalid bet. Bet must be $1 - $${c.balance}`;
            res.className = "status err";
            return;
          }
          const lucky = 1 + Math.floor(Math.random() * 10);
          if (picked === lucky) {
            const win = bet * 10;
            c.balance += win;
            res.textContent = `Fantastic! Guessed ${picked}, lucky was ${lucky}. Won $${win}.`;
            res.className = "status ok";
          } else {
            c.balance -= bet;
            res.textContent = `Unlucky. Guessed ${picked}, lucky was ${lucky}. Lost $${bet}.`;
            res.className = "status err";
          }
          if (c.balance <= 0) {
            alert(`Game Over. Balance hit $0. Good game, ${c.player}.`);
            c.started = false;
            c.player = "";
            c.balance = 0;
            renderCasino();
            return;
          }
          renderCasino();
        });

        el("casQuit").addEventListener("click", () => {
          alert(`Thanks, ${c.player}. Final balance: $${c.balance}`);
          c.started = false;
          c.player = "";
          c.balance = 0;
          renderCasino();
        });
      }

      function renderGuess() {
        const main = el("main");
        const g = state.guess;

        main.innerHTML = `
        <section class="panel vstack" style="max-width:760px;margin:0 auto;">
          <h2 style="margin:0;color:#00d4ff;">Mystery Number</h2>
          <div class="small">Guess the secret number from 1 to 10. You have 3 lives.</div>

          <div class="kpi">
            <div class="small">Lives Remaining</div>
            <div class="n">${"".repeat(g.lives) || "0"}</div>
            <div class="small">${g.count} / 3 guesses made</div>
          </div>

          <input id="gsIn" class="input" type="number" min="1" max="10" placeholder="Enter your guess" ${g.over ? "disabled" : ""} />
          <button id="gsBtn" class="btn" style="background:#00d4ff;color:#0a0e27;font-weight:700;" ${g.over ? "disabled" : ""}>Check Guess</button>
          <div id="gsFb" class="status">${g.over ? "Game finished. Start a new game." : ""}</div>
          <div class="small">Guesses: ${g.history.length ? g.history.join(" -> ") : "No guesses yet"}</div>
          <button id="gsReset" class="btn" style="background:#1a1f3a;color:#00ff88;font-weight:700;">New Game</button>
        </section>
      `;

        if (!g.over) {
          el("gsBtn").addEventListener("click", () => {
            const val = Number(el("gsIn").value.trim());
            const fb = el("gsFb");
            if (!Number.isInteger(val) || val < 1 || val > 10) {
              fb.textContent = "Enter an integer between 1 and 10.";
              fb.className = "status err";
              return;
            }
            g.count += 1;
            g.lives -= 1;
            g.history.push(val);

            if (val === g.secret) {
              g.over = true;
              fb.textContent = `Perfect! It was ${g.secret}. You got it in ${g.count} try(s).`;
              fb.className = "status ok";
              renderGuess();
              return;
            }

            if (g.lives <= 0) {
              g.over = true;
              fb.textContent = `Game Over! The secret was ${g.secret}.`;
              fb.className = "status err";
              renderGuess();
              return;
            }

            fb.textContent = val < g.secret ? "Too low." : "Too high.";
            fb.className = "status warn";
            renderGuess();
          });
        }

        el("gsReset").addEventListener("click", () => {
          state.guess = {
            secret: 1 + Math.floor(Math.random() * 10),
            lives: 3,
            count: 0,
            over: false,
            history: [],
          };
          renderGuess();
        });
      }

      function boot() {
        initNav();
        quizReset();
        showHome();
      }

      boot();

