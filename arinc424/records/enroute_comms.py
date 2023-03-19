from arinc424.decoder import Field
import arinc424.decoder as decoder


class EnrouteComms():

    cont_idx = 55
    app_idx = 56

    def read(self, r):
        if int(r[self.cont_idx]) < 2:
            return self.read_primary(r)
        else:
            match r[self.app_idx]:
                case ' ':
                    return self.read_cont(r)
                case 'T':
                    return self.read_timeop(r)
                case _:
                    raise ValueError('{}\n{}\n{}'.format("Unknown Application",
                                                         r[self.app_idx], r))

    def read_primary(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("FIR/RDO Ident",                       r[6:10],       decoder.field_190),
            Field("FIR/UIR Address",                     r[10:14],      decoder.field_151),
            Field("Indicator",                           r[14],         decoder.field_117),
            Field("Remote Name",                         r[18:43],      decoder.field_189),
            Field("Communications Type",                 r[43:46],      decoder.field_101),
            Field("Comm Frequency",                      r[46:53],      decoder.field_103),
            Field("Guard/Transmit",                      r[53],         decoder.field_182),
            Field("Frequency Units",                     r[54],         decoder.field_104),
            Field("Continuation Record No",              r[55],         decoder.field_016),
            Field("Service Indicator",                   r[56:59],      decoder.field_106),
            Field("Radar Service",                       r[59],         decoder.field_102),
            Field("Modulation",                          r[60],         decoder.field_198),
            Field("Signal Emission",                     r[61],         decoder.field_199),
            Field("Latitude",                            r[62:71],      decoder.field_036),
            Field("Longitude",                           r[71:81],      decoder.field_037),
            Field("Magnetic Variation",                  r[81:86],      decoder.field_039),
            Field("Facility Elevation",                  r[86:91],      decoder.field_092),
            Field("H24 Indicator",                       r[91],         decoder.field_181),
            Field("Altitude Description",                r[92],         decoder.field_029),
            Field("Communication Altitude",              r[93:98],      decoder.field_184),
            Field("Communication Altitude (2)",          r[98:103],     decoder.field_184),
            Field("Remote Facility",                     r[103:107],    decoder.field_200),
            Field("ICAO Code",                           r[107:109],    decoder.field_014),
            Field("Section Code (2)",                    r[109:111],    decoder.field_004),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    def read_cont(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("FIR/RDO Ident",                       r[6:10],       decoder.field_190),
            Field("FIR/UIR Address",                     r[10:14],      decoder.field_151),
            Field("Indicator",                           r[14],         decoder.field_117),
            Field("Remote Name",                         r[18:43],      decoder.field_189),
            Field("Communications Type",                 r[43:46],      decoder.field_101),
            Field("Comm Frequency",                      r[46:53],      decoder.field_103),
            Field("Guard/Transmit",                      r[53],         decoder.field_182),
            Field("Frequency Units",                     r[54],         decoder.field_104),
            Field("Continuation Record No",              r[55],         decoder.field_016),
            Field("Application Type",                    r[56],         decoder.field_091),
            Field("Time Code",                           r[57],         decoder.field_131),
            Field("NOTAM",                               r[58],         decoder.field_132),
            Field("Time Indicator",                      r[59],         decoder.field_138),
            Field("Time of Operation",                   r[60:70],      decoder.field_195),
            Field("Call Sign",                           r[93:123],     decoder.field_105),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]

    def read_timeop(self, r):
        return [
            Field("Record Type",                         r[0],          decoder.field_002),
            Field("Customer / Area Code",                r[1:4],        decoder.field_003),
            Field("Section Code",                        r[4:6],        decoder.field_004),
            Field("FIR/RDO Ident",                       r[6:10],       decoder.field_190),
            Field("FIR/UIR Address",                     r[10:14],      decoder.field_151),
            Field("Indicator",                           r[14],         decoder.field_117),
            Field("Remote Name",                         r[18:43],      decoder.field_189),
            Field("Communications Type",                 r[43:46],      decoder.field_101),
            Field("Comm Frequency",                      r[46:53],      decoder.field_103),
            Field("Guard/Transmit",                      r[53],         decoder.field_182),
            Field("Frequency Units",                     r[54],         decoder.field_104),
            Field("Continuation Record No",              r[55],         decoder.field_016),
            Field("Application Type",                    r[56],         decoder.field_091),
            Field("Time of Operation",                   r[60:70],      decoder.field_195),
            Field("Time of Operation (2)",               r[70:80],      decoder.field_195),
            Field("Time of Operation (3)",               r[80:90],      decoder.field_195),
            Field("Time of Operation (4)",               r[90:100],     decoder.field_195),
            Field("Time of Operation (5)",               r[100:110],    decoder.field_195),
            Field("Time of Operation (6)",               r[110:120],    decoder.field_195),
            Field("File Record No",                      r[123:128],    decoder.field_031),
            Field("Cycle Date",                          r[128:132],    decoder.field_032)
        ]
