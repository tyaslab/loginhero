def auto_trim(value):
    if isinstance(value, str):
        return value.strip()
    
    if isinstance(value, dict):
        result = {}
        for key in value:
            result[key] = auto_trim(value[key])
        
        return result
    
    if isinstance(value, list):
        result = []
        for k, v in enumerate(value):
            result.append(auto_trim(v))
        
        return result
    
    return value
