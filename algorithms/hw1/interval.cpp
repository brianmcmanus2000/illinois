#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <fftw3.h>
void print_set(std::set<int> set){
    std::set<int>::iterator i;
    for(i = set.begin(); i != set.end(); i++){
        std::cout<<*i << ", ";
    }
    std::cout << std::endl;
}
#include <iostream>
#include <vector>
#include <set>
#include <fftw3.h>

void count_distinct_interval_sums(const std::vector<int>& A) {
    int total_sum = 0;
    for (int num : A) {
        total_sum += num;
    }

    int size = total_sum + 1; // Reduced size because we only need non-negative sums
    std::vector<double> P(size, 0.0);
    P[0] = 1.0;  // Initialize polynomial to 1 at the start (representing sum 0)

    // Prepare FFTW arrays
    fftw_complex *in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * size);
    fftw_complex *out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * size);
    fftw_plan forward_plan = fftw_plan_dft_1d(size, in, out, FFTW_FORWARD, FFTW_ESTIMATE);
    fftw_plan inverse_plan = fftw_plan_dft_1d(size, out, in, FFTW_BACKWARD, FFTW_ESTIMATE);

    for (int a : A) {
        std::vector<double> new_P(size, 0.0);
        for (int i = 0; i < size - a; ++i) {
            new_P[i + a] = P[i];
        }

        // Perform FFT on P
        for (int i = 0; i < size; ++i) {
            in[i][0] = P[i];
            in[i][1] = 0.0;
        }
        fftw_execute(forward_plan);

        // Perform FFT on new_P
        for (int i = 0; i < size; ++i) {
            in[i][0] = new_P[i];
            in[i][1] = 0.0;
        }
        fftw_execute(forward_plan);

        // Multiply in frequency domain
        for (int i = 0; i < size; ++i) {
            double real_part = out[i][0];
            double imag_part = out[i][1];
            out[i][0] = real_part * in[i][0] - imag_part * in[i][1];
            out[i][1] = real_part * in[i][1] + imag_part * in[i][0];
        }

        // Perform inverse FFT
        fftw_execute(inverse_plan);

        // Normalize and update P
        for (int i = 0; i < size; ++i) {
            P[i] = in[i][0] / size;
        }
    }

    // Extract distinct sums
    std::set<int> distinct_sums;
    for (int i = 0; i < size; ++i) {
        if (P[i] > 1e-10) { // Using a small threshold to account for floating-point precision
            distinct_sums.insert(i);
        }
    }

    std::cout << "Number of distinct interval sums: " << distinct_sums.size() << std::endl;
    print_set(distinct_sums);
    // Cleanup FFTW
    fftw_destroy_plan(forward_plan);
    fftw_destroy_plan(inverse_plan);
    fftw_free(in);
    fftw_free(out);
}

int main() {
    std::vector<int> A = {8, 2, 3, 5};
    count_distinct_interval_sums(A);
    return 0;
}