#include <stdio.h>

#define C_RESET "\x1b[0m"
#define C_BLUE "\x1b[34m"
#define C_GREEN "\x1b[32m"
#define C_RED "\x1b[31m"

typedef struct
{
    int atomic_number;
    const char *symbol;
    const char *name;
} Element;

static const Element elements[] = {
    {1, "H", "Hydrogen"}, {2, "He", "Helium"}, {3, "Li", "Lithium"}, {4, "Be", "Beryllium"},
    {5, "B", "Boron"}, {6, "C", "Carbon"}, {7, "N", "Nitrogen"}, {8, "O", "Oxygen"},
    {9, "F", "Fluorine"}, {10, "Ne", "Neon"}, {11, "Na", "Sodium"}, {12, "Mg", "Magnesium"},
    {13, "Al", "Aluminium"}, {14, "Si", "Silicon"}, {15, "P", "Phosphorus"}, {16, "S", "Sulfur"},
    {17, "Cl", "Chlorine"}, {18, "Ar", "Argon"}, {19, "K", "Potassium"}, {20, "Ca", "Calcium"},
    {21, "Sc", "Scandium"}, {22, "Ti", "Titanium"}, {23, "V", "Vanadium"}, {24, "Cr", "Chromium"},
    {25, "Mn", "Manganese"}, {26, "Fe", "Iron"}, {27, "Co", "Cobalt"}, {28, "Ni", "Nickel"},
    {29, "Cu", "Copper"}, {30, "Zn", "Zinc"}, {31, "Ga", "Gallium"}, {32, "Ge", "Germanium"},
    {33, "As", "Arsenic"}, {34, "Se", "Selenium"}, {35, "Br", "Bromine"}, {36, "Kr", "Krypton"},
    {37, "Rb", "Rubidium"}, {38, "Sr", "Strontium"}, {39, "Y", "Yttrium"}, {40, "Zr", "Zirconium"},
    {41, "Nb", "Niobium"}, {42, "Mo", "Molybdenum"}, {43, "Tc", "Technetium"}, {44, "Ru", "Ruthenium"},
    {45, "Rh", "Rhodium"}, {46, "Pd", "Palladium"}, {47, "Ag", "Silver"}, {48, "Cd", "Cadmium"},
    {49, "In", "Indium"}, {50, "Sn", "Tin"}, {51, "Sb", "Antimony"}, {52, "Te", "Tellurium"},
    {53, "I", "Iodine"}, {54, "Xe", "Xenon"}, {55, "Cs", "Cesium"}, {56, "Ba", "Barium"},
    {57, "La", "Lanthanum"}, {58, "Ce", "Cerium"}, {59, "Pr", "Praseodymium"}, {60, "Nd", "Neodymium"},
    {61, "Pm", "Promethium"}, {62, "Sm", "Samarium"}, {63, "Eu", "Europium"}, {64, "Gd", "Gadolinium"},
    {65, "Tb", "Terbium"}, {66, "Dy", "Dysprosium"}, {67, "Ho", "Holmium"}, {68, "Er", "Erbium"},
    {69, "Tm", "Thulium"}, {70, "Yb", "Ytterbium"}, {71, "Lu", "Lutetium"}, {72, "Hf", "Hafnium"},
    {73, "Ta", "Tantalum"}, {74, "W", "Tungsten"}, {75, "Re", "Rhenium"}, {76, "Os", "Osmium"},
    {77, "Ir", "Iridium"}, {78, "Pt", "Platinum"}, {79, "Au", "Gold"}, {80, "Hg", "Mercury"},
    {81, "Tl", "Thallium"}, {82, "Pb", "Lead"}, {83, "Bi", "Bismuth"}, {84, "Po", "Polonium"},
    {85, "At", "Astatine"}, {86, "Rn", "Radon"}, {87, "Fr", "Francium"}, {88, "Ra", "Radium"},
    {89, "Ac", "Actinium"}, {90, "Th", "Thorium"}, {91, "Pa", "Protactinium"}, {92, "U", "Uranium"},
    {93, "Np", "Neptunium"}, {94, "Pu", "Plutonium"}, {95, "Am", "Americium"}, {96, "Cm", "Curium"},
    {97, "Bk", "Berkelium"}, {98, "Cf", "Californium"}, {99, "Es", "Einsteinium"}, {100, "Fm", "Fermium"},
    {101, "Md", "Mendelevium"}, {102, "No", "Nobelium"}, {103, "Lr", "Lawrencium"}, {104, "Rf", "Rutherfordium"},
    {105, "Db", "Dubnium"}, {106, "Sg", "Seaborgium"}, {107, "Bh", "Bohrium"}, {108, "Hs", "Hassium"},
    {109, "Mt", "Meitnerium"}, {110, "Ds", "Darmstadtium"}, {111, "Rg", "Roentgenium"}, {112, "Cn", "Copernicium"},
    {113, "Nh", "Nihonium"}, {114, "Fl", "Flerovium"}, {115, "Mc", "Moscovium"}, {116, "Lv", "Livermorium"},
    {117, "Ts", "Tennessine"}, {118, "Og", "Oganesson"}};

static const int element_count = (int)(sizeof(elements) / sizeof(elements[0]));

static const Element *find_element_by_atomic_number(int atomic_number)
{
    int i;
    for (i = 0; i < element_count; i++)
    {
        if (elements[i].atomic_number == atomic_number)
        {
            return &elements[i];
        }
    }
    return NULL;
}

static void print_element_card(const Element *e)
{
    printf(C_GREEN "\n+---------------- ELEMENT CARD ----------------+\n" C_RESET);
    printf("| Atomic Number : %-28d|\n", e->atomic_number);
    printf("| Symbol        : %-28s|\n", e->symbol);
    printf("| Name          : %-28s|\n", e->name);
    printf(C_GREEN "+----------------------------------------------+\n\n" C_RESET);
}

int main(void)
{
    int choice;

    printf(C_BLUE "========================================================\n" C_RESET);
    printf(C_BLUE "                MODERN PERIODIC TABLE HUB\n" C_RESET);
    printf(C_BLUE "========================================================\n" C_RESET);
    printf("Total elements indexed: %d\n\n", element_count);

    while (1)
    {
        int atomic_number;
        const Element *element;

        printf("1. Search by atomic number\n");
        printf("2. Exit\n");
        printf("Select: ");

        if (scanf("%d", &choice) != 1)
        {
            printf(C_RED "Invalid input. Closing app.\n" C_RESET);
            return 0;
        }

        if (choice == 2)
        {
            printf("Thanks for exploring chemistry.\n");
            break;
        }

        if (choice != 1)
        {
            printf(C_RED "Choose 1 or 2 only.\n\n" C_RESET);
            continue;
        }

        printf("Enter atomic number (1-118): ");
        if (scanf("%d", &atomic_number) != 1)
        {
            printf(C_RED "Invalid value. Closing app.\n" C_RESET);
            return 0;
        }

        element = find_element_by_atomic_number(atomic_number);
        if (element == NULL)
        {
            printf(C_RED "No element found for %d\n\n" C_RESET, atomic_number);
            continue;
        }

        print_element_card(element);
    }

    return 0;
}
