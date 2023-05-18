from data_tool_lib.timer_tasks import elapsed_time_process, elapsed_time_subprocess
import time

def print_division():
    print()
    print('=+'*50)
    print()

@elapsed_time_process
def func_1():
    '''Esta função realiza a tarefa 1'''
    time.sleep(5)
    print('PROCESSO func_1')

@elapsed_time_process
def func_2():
    '''Esta função realiza a tarefa 2'''
    time.sleep(7)
    print('PROCESSO func_2')

@elapsed_time_process
def func_3():
    '''Esta função realiza a tarefa 3'''

    @elapsed_time_subprocess
    def func_3_1():
        '''Esta função realiza a subtarefa 1'''
        time.sleep(2)
        print('PROCESSO INTERNO 3_1')
    
    @elapsed_time_subprocess
    def func_3_2():
        '''Esta função realiza a subtarefa 2'''
        time.sleep(2)
        print('PROCESSO INTERNO 3_2')
    
    func_3_1()
    func_3_2()
    return True
    

if __name__== '__main__':

    func_1()
    print_division()
    func_2()
    print_division()
    func_3()