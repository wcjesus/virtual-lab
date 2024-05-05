! sine_data.f90

program sine_data
    implicit none
    real :: x(100), y(100)
    integer :: i
    real :: frequency, amplitude, pi
    character(100) :: num1char
    character(100) :: num2char

    pi = 3.14159265358979323

    ! Read frequency and amplitude from command line
    call get_command_argument(1, num1char)
    call get_command_argument(2, num2char)


    read(num1char,*)frequency                    !then, convert to REAL
    read(num2char,*)amplitude                    !then, convert to REAL

    ! Generate data
    do i = 1, 100
        x(i) = i / 10.0
        y(i) = amplitude * sin(2.0 * pi * frequency * x(i))
    end do

    ! Write data to file
    open(unit=10, file='data.txt')
    do i = 1, 100
        write(10, *) x(i), y(i)
    end do
    close(unit=10)
end program sine_data
