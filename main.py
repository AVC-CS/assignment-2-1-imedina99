def main():

    m_perc = int(input('The number of males is '))
    f_perc = int(input('The number of females is '))
    total = m_perc + f_perc

    print(f'The total number of students is \t {total}')
    print (f'The percentage of males is \t {m_perc: .2f}')
    print (f'The percentage of females is \t {f_perc: .2f}')

    return m_perc, f_perc


if __name__ == '__main__':
    main()
