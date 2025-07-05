from bs4 import BeautifulSoup
from typing import List, Tuple, Set, Dict


def parse_mod_file(file_path) -> List[Tuple[str, str]]:
    """Parse an Arma 3 mod HTML file and return a list of mod dictionaries"""
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    mods = []
    for row in soup.select('tr[data-type="ModContainer"]'):
        
        name = row.find('td', {'data-type': 'DisplayName'}).text.strip(),
        url = row.find('a')['href'] if row.find('a') else None
        
        
        mods.append((name[0], url))
    return mods

def compare_mod_files(mod_list1: Set[Tuple[str, str]], 
                      mod_list2: Set[Tuple[str, str]],
                      verbose: bool = False) -> Dict[str, List[Tuple[str, str]]]:
    """
    Description:
    ----------
    This function takes two sets of tuples representing mods and checks their 
    set-wise relationship between one another.

    Parameters
    ----------
    mod_list1 : Set[Tuple[str, str]]
        Set of mods for file 1.
    mod_list2 : Set[Tuple[str, str]]
        Set of mods for file 2.
    verbose : bool, optional
        The default is False.

    Returns
    -------
    Dict[str, List[Tuple[str, str]]]
        DESCRIPTION.

    """
    
    """function that compares two mod lists and tells what the
    set-wise relations are

    Args:
        mod_list1 (Set[Mod]): Set of mods for file 1
        mod_list2 (Set[Mod]): Set of mods for file 2
    """ 
    
    common: List[Tuple[str, str]] = list(mod_list1 & mod_list2)
    unique : List[Tuple[str, str]] = list(mod_list1 | mod_list2)
    first_only: List[Tuple[str, str]] = list(mod_list1 - mod_list2)
    second_only: List[Tuple[str, str]]= list(mod_list2 - mod_list1)
    
    if verbose:
        print("Common mods:", common )  # Intersection
        print("All unique mods:", unique)  # Union
        print("Only in first set:", first_only)  # Difference
        print("Only in second set:", second_only)  # Difference
        print("Exclusive to each set:", mod_list1 ^ mod_list2)  # Symmetric difference
    
    return {'common': common,
            "unique": unique,
            "first only": first_only,
            "second only": second_only}
    
    
def fully_process(path1: str, path2: str) -> Dict[str, List[Tuple[str, str]]]:
    """
    Description:
    ----------
    this function fully processes the HTML files to extract 
    the mods in a dictionary.
    
    Parameters
    ----------
    path1 : str
        path towards first HTML file relative to cwd.
    path2 : str
        path towards second HTML file relative to cwd.

    Returns
    -------
    Dict[str, List[Tuple[str, str]]]
        Dictionary containing string keys together with lists of 
        2-string-tuples representing mods.
    """
    mods1: List[Tuple[str, str]] = parse_mod_file(path1)
    mods2: List[Tuple[str, str]] = parse_mod_file(path2)
    
    mod_set1: Set[Tuple[str, str]] = set(mods1)
    mod_set2: Set[Tuple[str, str]] = set(mods2)
    
    results_dict: Dict[str, Set[Tuple[str, str]]] = compare_mod_files(mod_set1, mod_set2)
    return results_dict


    
    