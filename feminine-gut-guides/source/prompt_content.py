# Phase 1 meal plan prompt for clients to paste into an AI assistant.
# Prompt wording is Lalita's; the client attaches only the hair analysis report,
# and the Dirty Dozen section is added at her request.

P_OPEN = ("pp", "Help me create a detailed four-week meal plan for Phase 1 of The Feminine Gut: Tune In, Eliminate Triggers & Meet Nutritional Needs.")
P_ATTACH = ("pp", "I am attaching my hair analysis report.")
P_READ = [
    ("ph", "Read my report first:"),
    ("pul", [
        "Check the report’s legend and identify foods labeled high reactivity, moderate reactivity, and green-dot items.",
        "Show me these three food lists for confirmation. Ask about anything unclear or unreadable.",
        "For Phase 1, temporarily avoid high and moderate reactivity items throughout all four weeks and build meals primarily around green-dot foods.",
        "Check every ingredient, including cooking oils, seasonings, sauces, dressings, beverages, and substitutions.",
        "Do not assume unlisted foods are green-dot items. Ask before including them.",
        "Treat these as the report’s categories, not medically confirmed sensitivities. Hair testing does not reliably establish food sensitivities, and green dots do not guarantee tolerance. Always respect known allergies, intolerances, and previous reactions.",
    ]),
    ("ph", "Shop with the Dirty Dozen in mind:"),
    ("pul", [
        "Use the Environmental Working Group’s (EWG) most recent Dirty Dozen list. In my menus and grocery lists, mark any Dirty Dozen produce as “buy organic.”",
        "If organic is unavailable or over budget, suggest frozen organic or a green-dot alternative from EWG’s Clean Fifteen list. Never substitute a high or moderate reactivity food.",
    ]),
]
P_ASK = [
    ("ph", "Before building my plan, ask me:"),
    ("pol", [
        "Has my practitioner reviewed my report and confirmed the temporary food exclusions?",
        "Do I have confirmed allergies, known intolerances, or foods that cause symptoms regardless of their report category?",
        "How many people am I feeding, and how many meals and snacks do I want daily?",
        "What is my weekly grocery budget, and where do I shop?",
        "What foods and cuisines do I enjoy or dislike?",
        "How much cooking time do I have, what equipment is available, and which ingredients do I already own?",
        "Has my healthcare professional given me nutrition targets or other dietary requirements?",
    ]),
    ("pp", "Wait for my answers and confirmation of the food lists before creating the plan."),
]
P_ORG = [
    ("ph", "Organize the plan into Week 1, Week 2, Week 3, and Week 4. For each week, include:"),
    ("pol", [
        "<b>A seven-day menu:</b> List each requested meal and snack, portions, recipe servings, and planned leftovers.",
        "<b>A weekly grocery list:</b> Group ingredients by category. Include quantities that match the recipes and household size, accounting for leftovers and ingredients carried over from previous weeks.",
        "<b>Complete recipes and cooking instructions:</b> Give exact ingredient amounts, preparation time, cooking time, temperatures, numbered steps, and servings for every unique recipe. Clearly reference any repeated recipes.",
        "<b>A weekly preparation schedule:</b> Explain what to batch-cook, prepare ahead, and cook fresh. Include safe storage, freezing, and reheating instructions.",
        "<b>Practical substitutions:</b> Offer affordable alternatives that follow the same food restrictions.",
    ]),
]
P_CLOSE = [
    ("pp", "Keep meals enjoyable, varied, and realistic. Reuse ingredients thoughtfully to reduce cost and waste while providing adequate energy, protein, fiber, and variety."),
    ("pp", "If the exclusions make a balanced plan difficult, flag this for my practitioner rather than adding more restrictions. Do not extend the elimination period beyond four weeks or create a reintroduction schedule without my practitioner’s guidance."),
]

PROMPT = {
    "slug": "Feminine_Gut_Phase_1_Meal_Plan_Prompt",
    "num": "07",
    "series": "Phase 1 Meal Plan",
    "pages": [
        {
            "title": "Your Phase 1 <em>Meal Plan Prompt</em>",
            "sub": "Tune In, Eliminate Triggers & Meet Nutritional Needs.",
            "blocks": [
                ("intro", "Use this prompt with an AI assistant to build a four-week Phase 1 meal plan around your hair analysis report, with the Dirty Dozen in mind."),
                ("trio", [
                    ("1. Gather", "Your hair analysis report, saved as a PDF or clear photos."),
                    ("2. Copy & attach", "Copy the full prompt (both pages) into the chat and attach your report."),
                    ("3. Answer", "Confirm the food lists and answer each question. Then review your finished plan with your practitioner."),
                ]),
                ("prompt", "start", [P_OPEN, P_ATTACH] + P_READ),
            ],
        },
        {
            "title": "Before <em>the Plan</em>",
            "sub": "The rest of your prompt: questions to answer and how your plan is organized.",
            "blocks": [
                ("prompt", "end", P_ASK + P_ORG + P_CLOSE),
                ("disclaimer", "Educational guidance. Follow your individual plan and discuss persistent symptoms or dietary restrictions with your healthcare provider. Avoid known allergens; recommendations should fit your needs."),
            ],
        },
    ],
}
