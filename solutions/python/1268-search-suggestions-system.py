class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Sort the product list 
        sorted_products = sorted(products) 
        result = [] 

        # Iterate over each prefix of the searchWord 
        for i in range(1, len(searchWord) + 1): 
            prefix = searchWord[:i] 

            # Find the starting position of the prefix in sorted products 
            idx = bisect_left(sorted_products, prefix) 
            suggestions = [] 

            # Collect up to 3 products as suggestions 
            for j in range(idx, min(idx + 3, len(sorted_products))): 
                if sorted_products[j].startswith(prefix): 
                    suggestions.append(sorted_products[j]) 

            result.append(suggestions) 

        return result 
                                                                                                                                                                                                                 
