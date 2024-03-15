class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 0:
            return 0

        compressed = []
        current_char = chars[0]
        count = 1

        for i in range(1, len(chars)):
            if chars[i] == current_char:
                count += 1
            else:
                compressed.append(current_char)
                if count > 1:
                    compressed.extend(list(str(count)))
                current_char = chars[i]
                count = 1

        compressed.append(current_char)
        if count > 1:
            compressed.extend(list(str(count)))

        chars[:len(compressed)] = compressed
        return len(compressed)

