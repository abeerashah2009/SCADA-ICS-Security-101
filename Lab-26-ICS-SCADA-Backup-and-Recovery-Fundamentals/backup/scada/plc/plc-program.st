PROGRAM Main
VAR
    Motor_Start : BOOL;
    Motor_Stop  : BOOL;
    Pump_Running : BOOL;
    Tank_Level : INT;
END_VAR

IF Motor_Start AND NOT Motor_Stop THEN
    Pump_Running := TRUE;
END_IF;

IF Motor_Stop THEN
    Pump_Running := FALSE;
END_IF;

END_PROGRAM
