# -*- coding: utf-8 -*-
import random

class QueryBuilder:
    def __init__(self):
        self.file_path = "database/database.txt"
    
    def get_categories(self):
        categories = set()
        
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(', ')
                if len(parts) > 3:
                    categories.add(parts[-1])
        
        return sorted(list(categories))
    
    def get_random_elements(self, level, categories, rounds):
        elements = []

        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                columns = line.strip().rsplit(", ", 3)

                if len(columns) == 4:
                    name, description, lvl, category = columns
                    try:
                        lvl = int(lvl)
                        if lvl == level and category in categories:
                            elements.append((name, description))
                    except ValueError:
                        print(f"Erreur de conversion pour la ligne : {line.strip()}")

        selected_elements = dict(random.sample(elements, min(rounds, len(elements))))

        return selected_elements
    
    def get_sorted_elements_by_level(self):
        elements = []

        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                columns = line.strip().split(", ")
                if len(columns) < 4:
                    continue

                name, description, level, category = columns[0], columns[1], columns[2].strip(), columns[3]

                try:
                    level = int(level)
                    elements.append((name, description, level))
                except ValueError:
                    continue

        sorted_elements = sorted(elements, key=lambda x: (
            x[2] != 0,
            x[2] not in (0, 1),
            x[2] != 1,
            x[2] not in (1, 2),
            x[2] != 2
        ))

        return {name: description for name, description, _ in sorted_elements}