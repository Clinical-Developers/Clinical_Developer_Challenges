Matt_Townend:

__global__ void InvertBitKernel(int *data, int *output, int count) {
 
    int idx = blockIdx.x*blockDim.x+threadIdx.x;
 
    int index = idx / (sizeof(int) * 8);
 
    if (index < count) {
 
        int bit = idx % (sizeof(int) * 8);
        data[index] ^= 1 << bit;
 
    }
 
}
 
__global__ void DemaxIntKernel(int *data, int *output, int count) {
 
    int idx = blockIdx.x*blockDim.x+threadIdx.x;
 
    if (idx < count) {
        output[idx] = (INT_MAX - data[idx]) + 1;
    }
 
 
}
 
void InvertIntegers(int* data, int count) {
 
    //Initialise pointers to hold the address of GPU memory for our data
    int* outputPointer;
    int* gpuPointer;
 
    //Allocate memory and copy across our accountancy data to THE IMMENSELY POWERFUL GTX1060 HAIL NVIDIA
    cudaMalloc((void **)&gpuPointer, sizeof(int) * count);  cudaMemcpy(gpuPointer, data, sizeof(int) * count, cudaMemcpyHostToDevice);
    cudaMalloc((void **)&outputPointer, sizeof(int) * count);   cudaMemset(outputPointer, 0, sizeof(int)* count);
    cudaMalloc((void **)&gpuPointer, sizeof(int) * count);  cudaMemcpy(gpuPointer, &data[0], sizeof(int) * count, cudaMemcpyHostToDevice);
 
   
    //Praise CUDA with ritualised prayers to optimise our GPU accelerated journey
    int minGridSize, blockSize, gridSize;
    cudaOccupancyMaxPotentialBlockSize(&minGridSize, &blockSize, InvertBitKernel, 0, 0);
    gridSize = ((sizeof(int) * 8 * count) + blockSize - 1) / blockSize;
   
    //Launch a thread on the GPU... FOR EVERY BIT IN OUR DATA, EACH WITH THE SOLE TASK OF INVERTING A SINGLE POINT OF MEMORY - TREMBLE BEFORE THE MIGHT OF OUR MULTICORED LORD
    InvertBitKernel<<<gridSize, blockSize>>>(gpuPointer, outputPointer, count);
   
   
    cudaOccupancyMaxPotentialBlockSize(&minGridSize, &blockSize, DemaxIntKernel, 0, 0);
    gridSize = (count + blockSize - 1) / blockSize;
   
    //LAUNCH ANOTHER KERNEL TO SORT OUT THE HAZY BITWISE MESS I CREATED WITH THE FIRST ONE
    DemaxIntKernel<<<gridSize, blockSize>>>(gpuPointer, outputPointer, count);
 
    //Retrieve our data and put it back where it belongs
    cudaMemcpy(&data[0], outputPointer, sizeof(int) * count, cudaMemcpyDeviceToHost);
 
    return;
}
