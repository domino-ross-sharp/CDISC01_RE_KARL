/*****************************************************************************\
*  ____                  _
* |  _ \  ___  _ __ ___ (_)_ __   ___
* | | | |/ _ \| '_ ` _ \| | '_ \ / _ \
* | |_| | (_) | | | | | | | | | | (_) |
* |____/ \___/|_| |_| |_|_|_| |_|\___/                                               
* ____________________________________________________________________________
* Sponsor              : Domino
* Study                : CDISC01
* Program              : ADSL.sas
* Purpose              : Create ADaM ADSL dummy dataset
* ____________________________________________________________________________
* DESCRIPTION                                                    
*                                                                   
* Input files:  SDTM: DM
*              
* Output files: adam.ADSL
*               
* Macros:       None
*         
* Assumptions: 
*
* ____________________________________________________________________________
* PROGRAM HISTORY                                                         
*  09MAY2023  | Megan Harries  | Original
* ----------------------------------------------------------------------------
\*****************************************************************************/

*********;
** Setup environment including libraries for this reporting effort;
%*include "/mnt/code/domino.sas";
*********;

libname inputs "/workflow/inputs";
libname outputs "/workflow/outputs";

data _null_;
   infile '/workflow/inputs/sdtm_dataset_snapshot' truncover;
   input data_path $CHAR100.;
   call symputx('data_path', data_path, 'G');
run;
libname sdtm "&sdtm_path.";

data outputs.adsl;
	set sdtm.dm;
run;