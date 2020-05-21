from Levenshtein import distance, ratio
import statistics

def similar(string, array):
    for i in array:
        return ratio(string, i)

def similarity_ratios(l):
    ratios = {}
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            ratios[(l[i], l[j])] = ratio(l[i], l[j])
    return ratios

def similarity_analysis(l):
    results = similarity_ratios(l)
    ratios = [ result for k, result in results.items() ]
    if len(ratios) == 1:
        return { "similarity": ratios[0] }
    else:
        return { "similarity": statistics.mean(ratios) }
