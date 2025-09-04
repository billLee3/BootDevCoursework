def count_nested_levels(nested_documents, target_document_id, level=1):
    dict = nested_documents.copy()
    for key in dict:
        if key == target_document_id:
            return level  
        else:
            res = count_nested_levels(dict[key], target_document_id, level+1) 
            if res != -1:
                return res
    return -1
