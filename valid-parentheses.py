class Solution:
    def isValid(self, s: str) -> bool:
        pila = []
        pil = []
        
        if len(s) <= 1:
            return False
        
        elif s[0] == "}" or s[0] == ")" or s[0] == "]":
            return False
        
        else:
            for i in s:
                if(i == "(" or i == "{" or i  == "["):
                    pila.append(i)
                    continue
                    
                elif len(pila) > 0:
                    if ( (pila[-1] == "(" and i == ")") or (pila[-1] == "[" and i == "]") or ((pila[-1] == "{" and i == "}") ) ):
                        del(pila[-1])
                        
                    else:
                        pil.append(i)
                        
                else: 
                    pil.append(i)    
                    
            if (len(pila) >0 or len(pil) > 0):
                return False

            else:
                return True
