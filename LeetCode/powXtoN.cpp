// 50. Pow(x, n)
class Solution {
public:
    double pow(double x, int n)
{
    if (n == 0)
        return 1;
    if (n == 1)
        return x;
    double intermidiate = pow(x, n / 2);
    if (n % 2 == 0)
        return intermidiate * intermidiate;
    else
        return intermidiate * intermidiate * x;
}
    double myPow(double x, int n)
    {
        double answer = pow(x, abs(n));

        if (n > 0)
            return answer;
        else
            return 1.0 / answer;
    }
};
