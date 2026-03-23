rule test_malware
{
    strings:
      $evil = "evil_string"
    condition:
      $evil
}