def transform_texts(texts):
    """
    Napisz funkcję, która przyjmuje listę napisów i zwraca listę przekształconych tekstów:
      1) bez pustych
      2) zamienione na wielkie litery,
      3) odwrócone (w sensie kolejności znaków).
    """
    
    # Odfiltruj puste napisy.
    # filtered_texts = [t for t in texts if ...]

    # Zastosuj map i lambda do przekształceń.
    # transformed = map(lambda t: ..., filtered_texts)

    # Zwróć wyniki w postaci listy.
    pass

if __name__ == '__main__':
    # Przykładowe wywołanie:
    sample_data = ["hello", "  ", "world", "", "python"]
    result = transform_texts(sample_data) # ['OLLEH', 'DLROW', 'NOHTYP']
    print("Dla danych:", sample_data)
    print("Wynik   :", result) 
