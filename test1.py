def getVMIp(vm_id):
    global user
    getVMIp_data = {'command': 'listVirtualMachines', 'id' : vm_id,'response':'json'}
    req_vmip = user.post(url,data=vm_data)
    vmip = req_vmip.json()

    return vmip