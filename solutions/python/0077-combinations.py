class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def generate_combinations(elems, num):
            elems_tuple = tuple(elems)
            total = len(elems_tuple)
            if num > total:
                return
            curr_indices = list(range(num))
            while True:
                yield tuple(elems_tuple[i] for i in curr_indices)
                for idx in reversed(range(num)):
                    if curr_indices[idx] != idx + total - num:
                        break
                else:
                    return
                curr_indices[idx] += 1
                for j in range(idx+1, num):
                    curr_indices[j] = curr_indices[j-1] + 1

        return [list(combination) for combination in generate_combinations(range(1, n+1), k)]
