# Sort Characters By Frequency
def frequencySort(s):
            freq = {}

            for ch in s:
                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1

            sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

            result = ""

            for char, count in sorted_chars:
                result += char * count

            return result
