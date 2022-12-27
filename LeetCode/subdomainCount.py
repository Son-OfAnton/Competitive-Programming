# https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_frequency = defaultdict(int)

        for cpdomain in cpdomains:
            cpdomain = cpdomain.split()
            frequency = int(cpdomain[0])
            subdomains = cpdomain[1].split(".")
            
            for index, domain in enumerate(subdomains):
                variation = [domain] + subdomains[index + 1:]
                variation = ".".join(variation)
                visit_frequency[variation] += frequency

        res = []

        for url, visit_count in visit_frequency.items():
            res.append("{} {}".format(visit_count, url))

        return res
