param([string]$Server,[string]$locusername,[string]$locpassword)

$password = "$locpassword" | ConvertTo-SecureString -asPlainText -Force 
$username = $locusername 
$cred = New-Object System.Management.Automation.PSCredential($username,$password)

$s = New-PSSession -ComputerName $Server -Credential $cred

Set-Item WSMan:\localhost\Client\TrustedHosts -Value "*" -Force

Invoke-Command {& "g:\sql2008r2\Setup.exe" /q /ConfigurationFile=g:\sql2008r2\File.ini} -Session $s