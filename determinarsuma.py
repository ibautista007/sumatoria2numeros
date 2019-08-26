class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Creacion de nuevo arreglo para tomar los valores evaluados previamente
        valor = {}
        
        #proceso de evaluacion de numeros
        
        for i in range(len(nums)):
            
            #revisar si se tiene el valor guardado, sino almacenar nuevo valor
            if target-nums[i] not in valor:
                valor[nums[i]]=i
            
            #si el valor esta, se mandara los resultados a pantalla
            else:
                return [valor[target-nums[i]],i]
            
            
        return (valor)
