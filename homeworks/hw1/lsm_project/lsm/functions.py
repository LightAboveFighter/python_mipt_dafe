"""
В этом модуле хранятся функции для применения МНК
"""


from typing import Optional
from numbers import Real       # раскомментируйте при необходимости

from lsm_project.event_logger.event_logger import EventLogger

from lsm_project.lsm.enumerations import MismatchStrategies
from lsm_project.lsm.models import (
    LSMDescription,
    LSMStatistics,
    LSMLines,
)

<<<<<<< HEAD
# import os
=======
import os
>>>>>>> ac9774b (add MNK HM 26.10.23)


PRECISION = 3                   # константа для точности вывода
event_logger = EventLogger()    # для логирования


def get_lsm_description(
    abscissa: list[float], ordinates: list[float],
    mismatch_strategy: MismatchStrategies = MismatchStrategies.CUT
) -> LSMDescription:
    """
    Функции для получения описания рассчитаной зависимости

    :param: abscissa - значения абсцисс
    :param: ordinates - значение ординат
    :param: mismatch_strategy - стратегия обработки несовпадения

    :return: структура типа LSMDescription
    """

    min_list_length = 2

    global event_logger

    if not isinstance(abscissa, list):
        if not (list(abscissa)):
            event_logger.error("Can't turn abscissa into list")
            raise TypeError
        abscissa = list(abscissa)
    if not isinstance(ordinates, list):
        if not (list(ordinates)):
            event_logger.error("Can't turn ordinates into list")
            raise TypeError
        ordinates = list(ordinates)

<<<<<<< HEAD
    if len(abscissa) <= min_list_length or len(ordinates) <= min_list_length:
        event_logger.error(f"Lenght of abscissa or ordinates is lesser {min_list_length + 1}")
=======
    if len(abscissa) <= 2 or len(ordinates) <= 2:
        event_logger.error("Lenght of abscissa or ordinates is lesser 3")
>>>>>>> ac9774b (add MNK HM 26.10.23)
        raise ValueError

    if len(abscissa) != len(ordinates):
        abscissa, ordinates = _process_mismatch(abscissa, ordinates, mismatch_strategy)
<<<<<<< HEAD
    # if not _is_valid_measurments(abscissa + ordinates):
    #     event_logger.error("Wrong type abscissa - ordinates lists' members")
    #     raise ValueError
    if not _is_valid_measurments(abscissa):
        event_logger.error("Wrong type abscissa - list's members")
        raise ValueError
    if not _is_valid_measurments(ordinates):
        event_logger.error("Wrong type ordinates list's members")
        raise ValueError

    description = _get_lsm_description(abscissa, ordinates)
    # ваш код
    # эту строчку можно менять
    return description
=======
    if not _is_valid_measurments(abscissa + ordinates):
        event_logger.error("Wrong type abscissa - ordinates lists' members")
        raise ValueError

    description = _get_lsm_description(abscissa, ordinates)
    incline = description.incline
    shift = description.shift
    incline_error = description.incline_error
    shift_error = description.shift_error
    # ваш код
    # эту строчку можно менять
    return LSMDescription(
        incline,
        shift,
        incline_error,
        shift_error
    )
>>>>>>> ac9774b (add MNK HM 26.10.23)


def get_lsm_lines(
    abscissa: list[float], ordinates: list[float],
    lsm_description: Optional[LSMDescription] = None
) -> LSMLines:
    """
    Функция для расчета значений функций с помощью результатов МНК

    :param: abscissa - значения абсцисс
    :param: ordinates - значение ординат
    :param: lsm_description - описание МНК

    :return: структура типа LSMLines
    """

    if lsm_description is None:
        lsm_description = get_lsm_description(abscissa, ordinates, MismatchStrategies.CUT)
    elif not isinstance(lsm_description, LSMDescription):
        event_logger.error("Wrong type of lms_description")
        raise TypeError

    event_logger.info("Started calculating lines: predicted, above and under")

    a, b = lsm_description.incline, lsm_description.shift
    error_rate_a = lsm_description.incline_error

    error_rate_b = lsm_description.shift_error

<<<<<<< HEAD
    line_predicted = [b + a * abscissa[i] for i in range(len(abscissa))]
    line_above = [(a + error_rate_a) * abscissa[i] +
                  b + error_rate_b for i in range(len(abscissa))]
    line_under = [(a - error_rate_a) * abscissa[i] +
                  b - error_rate_b for i in range(len(abscissa))]

    # line_predicted = []
    # line_above = []
    # line_under = []
    # for i in range(len(abscissa)):
    #     predicted_elem = b + a * abscissa[i]
    #     above_elem = (a + error_rate_a) * abscissa[i] + b + error_rate_b
    #     under_elem = (a - error_rate_a) * abscissa[i] + b - error_rate_b
    #     line_predicted.append(predicted_elem)
    #     line_above.append(above_elem)
    #     line_under.append(under_elem)
=======
    line_predicted = []
    line_above = []
    line_under = []

    for i in range(len(abscissa)):
        line_predicted.append(b + a * abscissa[i])
        line_above.append((a + error_rate_a) * abscissa[i] + b + error_rate_b)
        line_under.append((a - error_rate_a) * abscissa[i] + b - error_rate_b)
>>>>>>> ac9774b (add MNK HM 26.10.23)
    event_logger.info("Calculated lines: predicted, above and under")

    # ваш код
    # эту строчку можно менять
    return LSMLines(
        abscissa,
        ordinates,
        line_predicted,
        line_above,
        line_under
    )


def get_report(
    lsm_description: LSMDescription, path_to_save: str = ''
) -> str:
    """
    Функция для формирования отчета о результатах МНК

    :param: lsm_description - описание МНК
    :param: path_to_save - путь к файлу для сохранения отчета

    :return: строка - отчет определенного формата
    """
    global PRECISION
    size_str_report = 100
    char_end_report = "="
    report_lines = ["LSM computing result".center(size_str_report, char_end_report) + "\n",
                    f"[INFO]: incline: {lsm_description.incline:.{PRECISION}f};",
                    f"[INFO]: shift: {lsm_description.shift:.{PRECISION}f};",
                    f"[INFO]: incline error: {lsm_description.incline_error:.{PRECISION}f};",
                    f"[INFO]: shift error: {lsm_description.shift_error:.{PRECISION}f};\n",
                    size_str_report*char_end_report
                    ]

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    # report = "LSM computing result".center(100, "=") + "\n"
    # report.join("\n", f"[INFO]: incline: {lsm_description.incline:.{PRECISION}f};\n")
    # report += f"[INFO]: shift: {lsm_description.shift:.{PRECISION}f};\n"
    # report += f"[INFO]: incline error: {lsm_description.incline_error:.{PRECISION}f};\n"
    # report += f"[INFO]: shift error: {lsm_description.shift_error:.{PRECISION}f};\n\n"
    # report += 100*"="
    report = "\n".join(report_lines)
    if path_to_save:
        # if os.path.exists(path_to_save):
        file = open(path_to_save, "w")
        file.write(report)
        file.close()
        event_logger.info("Report saved to file")
        # else:
        #     event_logger.warning("Report path doesn't exist")
=======
    report = ("========================================LSM computing result" +
              "========================================\n\n[INFO]: incline:" +
              f" {lsm_description.incline:.{PRECISION}f};\n[INFO]: shift:" +
              f" {lsm_description.shift:.{PRECISION}f};\n[INFO]: incline error:" +
              f" {lsm_description.incline_error:.{PRECISION}f};\n" +
              f"[INFO]: shift error: {lsm_description.shift_error:.{PRECISION}f}" +
              ";\n\n====================================================" +
              "================================================")

=======
=======
>>>>>>> 4e5463d (add 27.10.23 MNK HM)
    report = "LSM computing result".center(100, "=") + "\n\n"
    report += f"[INFO]: incline: {lsm_description.incline:.{PRECISION}f};\n"
    report += f"[INFO]: shift: {lsm_description.shift:.{PRECISION}f};\n"
    report += f"[INFO]: incline error: {lsm_description.incline_error:.{PRECISION}f};\n"
    report += f"[INFO]: shift error: {lsm_description.shift_error:.{PRECISION}f};\n\n"
    report += 100*"="
<<<<<<< HEAD
>>>>>>> 9aab8e6 (add 27.10.23 MNK HM)
=======
>>>>>>> 4e5463d (add 27.10.23 MNK HM)
    if len(path_to_save) != 0:
        if os.path.exists(path_to_save):
            file = open(path_to_save, "w")
            file.write(report)
            file.close()
            event_logger.info("Report saved to file")
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ac9774b (add MNK HM 26.10.23)
=======
        else:
            event_logger.warning("Report path doesn't exist")
>>>>>>> 9aab8e6 (add 27.10.23 MNK HM)
=======
        else:
            event_logger.warning("Report path doesn't exist")
>>>>>>> 4e5463d (add 27.10.23 MNK HM)
    # ваш код
    # эту строчку можно менять
    return report


# служебная функция для валидации
def _is_valid_measurments(measurments: list[float]) -> bool:
<<<<<<< HEAD
    for elem in measurments:
        if not isinstance(elem, Real):
=======
    for i in range(len(measurments)):
        if not (isinstance(measurments[i], Real)):
>>>>>>> ac9774b (add MNK HM 26.10.23)
            return False

    # ваш код
    # эту строчку можно менять
    return True


# служебная функция для обработки несоответствия размеров
def _process_mismatch(
    abscissa: list[float], ordinates: list[float],
    mismatch_strategy: MismatchStrategies = MismatchStrategies.FALL
) -> tuple[list[float], list[float]]:
    global event_logger

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    # if len(abscissa) != len(ordinates):
    if mismatch_strategy == MismatchStrategies.FALL:
        event_logger.error("MismatchStrategies.FALL")
        raise RuntimeError
    elif mismatch_strategy == MismatchStrategies.CUT:
        abs_changed, ord_changed = abscissa, ordinates

        event_logger.info("Turning abscissa and ordinates into same lenght")
        min_len = min(len(abscissa), len(ordinates))
        abs_changed = abscissa[:min_len]
        ord_changed = ordinates[:min_len]
        event_logger.warning("Some elements of abscissa/ordinates were removed")
        return abs_changed, ord_changed
    else:
        event_logger.error("Incorrect mismatch strategy")
        raise ValueError

    # ваш код
    # эту строчку можно менять
    return abscissa, ordinates
=======
    abs_changed, ord_changed = abscissa, ordinates

=======
>>>>>>> 9aab8e6 (add 27.10.23 MNK HM)
=======
>>>>>>> 4e5463d (add 27.10.23 MNK HM)
    if len(abscissa) != len(ordinates):
        if mismatch_strategy == MismatchStrategies.FALL:
            event_logger.error("MismatchStrategies.FALL")
            raise RuntimeError
        elif mismatch_strategy == MismatchStrategies.CUT:
            abs_changed, ord_changed = abscissa, ordinates

            event_logger.info("Turning abscissa and ordinates into same lenght")
            min_len = min(len(abscissa), len(ordinates))
            abs_changed = abscissa[:min_len]
            ord_changed = ordinates[:min_len]
            event_logger.warning("Some elements of abscissa/ordinates were removed")
            return abs_changed, ord_changed
        else:
            event_logger.error("Incorrect mismatch strategy")
            raise ValueError

    # ваш код
    # эту строчку можно менять
<<<<<<< HEAD
<<<<<<< HEAD
    return abs_changed, ord_changed
>>>>>>> ac9774b (add MNK HM 26.10.23)
=======
    return abscissa, ordinates
>>>>>>> 9aab8e6 (add 27.10.23 MNK HM)
=======
    return abscissa, ordinates
>>>>>>> 4e5463d (add 27.10.23 MNK HM)


# служебная функция для получения статистик
def _get_lsm_statistics(
    abscissa: list[float], ordinates: list[float]
) -> LSMStatistics:
    global event_logger, PRECISION

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    event_logger.info("Started calculating average components")
=======
>>>>>>> ac9774b (add MNK HM 26.10.23)
=======
    event_logger.info("Started calculating average components")
>>>>>>> 9aab8e6 (add 27.10.23 MNK HM)
=======
    event_logger.info("Started calculating average components")
>>>>>>> 4e5463d (add 27.10.23 MNK HM)
    n = len(abscissa)

    abscissa_mean = sum(abscissa)/n
    ordinate_mean = sum(ordinates)/n
<<<<<<< HEAD
    abs_squared_mean = sum([elem**2 for elem in abscissa])/n
    product_mean = sum([elem_a*elem_o for (elem_a, elem_o) in zip(abscissa, ordinates)])/n

=======

    abs_squared_mean = 0
    product_mean = 0
    for i in range(n):
        abs_squared_mean += abscissa[i]**2
        product_mean += abscissa[i]*ordinates[i]

    abs_squared_mean = abs_squared_mean/n
    product_mean = product_mean/n
>>>>>>> ac9774b (add MNK HM 26.10.23)
    event_logger.info("Average components calculated")

    # ваш код
    # эту строчку можно менять
    return LSMStatistics(
        abscissa_mean,
        ordinate_mean,
        product_mean,
        abs_squared_mean
    )


# служебная функция для получения описания МНК
def _get_lsm_description(
    abscissa: list[float], ordinates: list[float]
) -> LSMDescription:
    global event_logger, PRECISION

    n = len(abscissa)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    stata = _get_lsm_statistics(abscissa, ordinates)
=======
    event_logger.info("Started calculating")
    stata = _get_lsm_statistics(abscissa, ordinates)

>>>>>>> ac9774b (add MNK HM 26.10.23)
=======
    stata = _get_lsm_statistics(abscissa, ordinates)
>>>>>>> 9aab8e6 (add 27.10.23 MNK HM)
=======
    stata = _get_lsm_statistics(abscissa, ordinates)
>>>>>>> 4e5463d (add 27.10.23 MNK HM)
    av_abs = stata.abscissa_mean
    av_ord = stata.ordinate_mean
    av_qrt_abs = stata.abs_squared_mean
    av_product = stata.product_mean

    incline = (av_product - av_abs * av_ord) / (av_qrt_abs - av_abs**2)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    event_logger.info("Line: Incline calculated")
    shift = av_ord - incline * av_abs
    event_logger.info("Line: Shift calculated")
=======
    event_logger.info("Incline calculated")
    shift = av_ord - incline * av_abs
    event_logger.info("Shift calculated")
>>>>>>> ac9774b (add MNK HM 26.10.23)
=======
    event_logger.info("Line: Incline calculated")
    shift = av_ord - incline * av_abs
    event_logger.info("Line: Shift calculated")
>>>>>>> 9aab8e6 (add 27.10.23 MNK HM)
=======
    event_logger.info("Line: Incline calculated")
    shift = av_ord - incline * av_abs
    event_logger.info("Line: Shift calculated")
>>>>>>> 4e5463d (add 27.10.23 MNK HM)

    disp_res = 0
    for i in range(n):
        disp_res += (ordinates[i] - incline * abscissa[i] - shift) ** 2
    disp_res /= (n - 2)

    incline_error = (disp_res / (n * (av_qrt_abs - av_abs**2))) ** 0.5
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    event_logger.info("Line: Incline error calculated")

    shift_error = ((disp_res * av_qrt_abs) / (n * (av_qrt_abs - av_abs**2))) ** 0.5
    event_logger.info("Line: Shift error calculated")
=======
    event_logger.info("Incline error calculated")

    shift_error = ((disp_res * av_qrt_abs) / (n * (av_qrt_abs - av_abs**2))) ** 0.5
    event_logger.info("Shift error calculated")
>>>>>>> ac9774b (add MNK HM 26.10.23)
=======
    event_logger.info("Line: Incline error calculated")

    shift_error = ((disp_res * av_qrt_abs) / (n * (av_qrt_abs - av_abs**2))) ** 0.5
    event_logger.info("Line: Shift error calculated")
>>>>>>> 9aab8e6 (add 27.10.23 MNK HM)
=======
    event_logger.info("Line: Incline error calculated")

    shift_error = ((disp_res * av_qrt_abs) / (n * (av_qrt_abs - av_abs**2))) ** 0.5
    event_logger.info("Line: Shift error calculated")
>>>>>>> 4e5463d (add 27.10.23 MNK HM)

    # ваш код
    # эту строчку можно менять
    return LSMDescription(
        incline,
        shift,
        incline_error,
        shift_error
    )
